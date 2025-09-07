#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "textual",
# ]
# ///

from textual.app import App
from textual.widget import Widget
from textual.widgets import Header, Footer
from textual.reactive import reactive

MAX_INVADERS = 10  # Total number of invaders to spawn


class InvaderGame(Widget):
    BINDINGS = [
        ("left", "move_left", "Move Left"),
        ("right", "move_right", "Move Right"),
        ("space", "shoot", "Shoot"),
        ("q", "quit", "Quit"),
        ("r", "restart", "Restart"),
    ]
    invader = "👾"
    spaceship = "🛸"
    shot = "️|"

    player_x = reactive(0)
    shots: list[tuple[int, int]] = reactive([])  # type: ignore
    invaders = reactive([])  # type: ignore
    direction = reactive(1)
    invader_speed = 15  # invader moves every 15 ticks (adjust for slower/faster)
    tick_count = 0
    game_over = reactive(False)
    game_message = reactive("")
    initialized = False
    can_focus = True

    def on_mount(self) -> None:
        # Set tick interval for ~30 FPS for smoother gameplay
        self.set_interval(1 / 30, self.game_tick)
        self.focus()

    def on_resize(self) -> None:
        width, height = self.size.width, self.size.height
        if width == 0 or height == 0:
            return
        if not self.initialized or self.game_over:
            self.player_x = width // 2

            # Calculate rows and cols to fit MAX_INVADERS given terminal size
            max_rows = height // 2
            max_cols = width // 2
            total_possible = max_rows * max_cols

            invader_count = min(MAX_INVADERS, total_possible)

            rows = min(max_rows, (invader_count + max_cols - 1) // max_cols)
            cols = min(
                max_cols,
                invader_count if rows == 1 else (invader_count + rows - 1) // rows,
            )

            total_invader_width = cols * 2 - 1
            start_x = max((width - total_invader_width) // 2, 0)

            self.invaders = []
            count = 0
            for y in range(rows):
                for x in range(cols):
                    if count >= invader_count:
                        break
                    self.invaders.append((start_x + x * 2, y + 1))
                    count += 1

            self.shots = []
            self.direction = 1
            self.tick_count = 0
            self.game_over = False
            self.game_message = ""
            self.initialized = True
            self.refresh()

    def game_tick(self) -> None:
        if self.game_over or not self.initialized:
            return
        self.tick_count += 1
        # Always move shots and detect collisions every frame for accuracy
        self.move_shots()
        self.detect_collisions()

        # Move invaders only every invader_speed ticks to slow movement
        if self.tick_count >= self.invader_speed:
            self.tick_count = 0
            self.move_invaders()

        self.refresh()

    def move_invaders(self) -> None:
        width, height = self.size.width, self.size.height
        if not self.invaders:
            return

        xs = [x for x, y in self.invaders]
        leftmost = min(xs)
        rightmost = max(xs)

        if (self.direction == 1 and rightmost >= width - 1) or (
            self.direction == -1 and leftmost <= 0
        ):
            self.invaders = [(x, y + 1) for x, y in self.invaders]
            self.direction *= -1
        else:
            self.invaders = [(x + self.direction, y) for x, y in self.invaders]

        if any(y >= height - 2 for _, y in self.invaders):
            self.game_over = True
            self.game_message = "Game Over! Invaders reached the bottom."
            self.refresh()

    def move_shots(self) -> None:
        # Move shots up and remove those above screen
        self.shots = [(x, y - 1) for x, y in self.shots if y > 0]

    def detect_collisions(self) -> None:
        remaining_invaders = []
        hit_shots = set()
        for inv_x, inv_y in self.invaders:
            hit = False
            for i, (shot_x, shot_y) in enumerate(self.shots):
                # If shot is at same position as invader
                if shot_x == inv_x and shot_y == inv_y:
                    hit = True
                    hit_shots.add(i)
                    break
                # If shot just passed through invader (shot_y == inv_y + 1 or shot_y == inv_y - 1)
                if shot_x == inv_x and (shot_y == inv_y + 1 or shot_y == inv_y - 1):
                    hit = True
                    hit_shots.add(i)
                    break
            if not hit:
                remaining_invaders.append((inv_x, inv_y))
        # Remove hit shots
        self.shots = [s for i, s in enumerate(self.shots) if i not in hit_shots]
        self.invaders = remaining_invaders

        if not self.invaders:
            self.game_over = True
            self.game_message = "You Win! All invaders are destroyed!"
            self.refresh()

    def render(self) -> str:
        width, height = self.size.width, self.size.height
        if self.game_over:
            blank_lines = (height - 3) // 2
            lines = [" " * width] * blank_lines
            lines.append(self.game_message.center(width))
            lines.append("Press Q to quit or R to restart".center(width))
            lines.extend([" " * width] * (height - blank_lines - 2))
            return "\n".join(lines)

        field = [[" " for _ in range(width)] for _ in range(height)]

        for x, y in self.invaders:
            if 0 <= x < width and 0 <= y < height:
                field[y][x] = self.invader

        for x, y in self.shots:
            if 0 <= x < width and 0 <= y < height:
                field[y][x] = self.shot

        player_y = height - 2
        if 0 <= self.player_x < width:
            field[player_y][self.player_x] = self.spaceship

        return "\n".join("".join(row) for row in field)

    def action_move_left(self) -> None:
        if self.player_x > 0:
            self.player_x -= 1
            self.refresh()

    def action_move_right(self) -> None:
        if self.player_x < self.size.width - 1:
            self.player_x += 1
            self.refresh()

    def action_shoot(self) -> None:
        shot_start = (self.player_x, self.size.height - 3)
        self.shots.append(shot_start)
        self.refresh()

    def action_quit(self) -> None:
        self.app.exit()

    def action_restart(self) -> None:
        self.initialized = False
        self.on_resize()


class InvaderApp(App):
    def compose(self):
        yield Header()
        yield Footer()
        yield InvaderGame()


if __name__ == "__main__":
    InvaderApp().run()
