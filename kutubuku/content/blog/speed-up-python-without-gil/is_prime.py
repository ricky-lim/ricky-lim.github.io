#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# ///

import math
from threading import Thread

PRIME_TEST_CASES = [
    (2, True),
    (142702110479723, True),
    (299593572317531, True),
    (3333333333333301, True),
    (3333333333333333, False),
    (3333335652092209, False),
    (4444444444444423, True),
    (4444444444444444, False),
    (4444444488888889, False),
    (5555553133149889, False),
    (5555555555555503, True),
    (5555555555555555, False),
    (6666666666666666, False),
    (6666666666666719, True),
    (6666667141414921, False),
    (7777777536340681, False),
    (7777777777777753, True),
    (7777777777777777, False),
    (9999999999999917, True),
    (9999999999999999, False),
    (11111111111111131, False),
    (22222222222222243, False),
    (33333333333333353, False),
    (44444444444444459, False),
    (55555555555555561, False),
    (66666666666666671, False),
    (77777777777777773, False),
    (88888888888888889, True),
    (99999999999999997, True),
    (12345678901234567, False),
]

NUMBERS = [n for n, _ in PRIME_TEST_CASES]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


class IsPrimeWorker:
    def __init__(self, n):
        self.n = n
        self.name = hash(n)
        self.result = None

    def run(self):
        self.result = is_prime(self.n)

    @classmethod
    def create_workers(cls):
        return [cls(n) for n in NUMBERS]


def main():
    workers = IsPrimeWorker.create_workers()
    threads = [Thread(target=worker.run) for worker in workers]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Check results
    print("Verifying results...")
    for (n, expected), worker in zip(PRIME_TEST_CASES, workers):
        assert (
            worker.result == expected
        ), f"Expected {n} to be {'prime' if expected else 'not prime'}, got {worker.result}"
    print(f"All {len(PRIME_TEST_CASES)} tests passed!")


if __name__ == "__main__":
    main()
