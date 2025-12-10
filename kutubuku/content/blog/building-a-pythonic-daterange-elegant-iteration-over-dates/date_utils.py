from datetime import date, timedelta
from typing import Iterator


def date_range(start_date: str, end_date: str) -> Iterator[str]:
    """
    Generate dates between start_date (inclusive) and end_date (inclusive).

    Args:
        start_date: ISO format date string "YYYY-MM-DD"
        end_date: ISO format date string "YYYY-MM-DD"

    Yields:
        str: Date strings in ISO format "YYYY-MM-DD"

    Examples:
        Basic usage:
        >>> list(date_range("2025-12-01", "2025-12-05"))
        ['2025-12-01', '2025-12-02', '2025-12-03', '2025-12-04', '2025-12-05']

        Year boundary:
        >>> list(date_range("2025-12-31", "2026-01-02"))
        ['2025-12-31', '2026-01-01', '2026-01-02']

        Leap year:
        >>> list(date_range("2024-02-28", "2024-03-01"))
        ['2024-02-28', '2024-02-29', '2024-03-01']

        Single day:
        >>> list(date_range("2025-12-07", "2025-12-07"))
        ['2025-12-07']

        Count days:
        >>> len(list(date_range("2025-01-01", "2025-12-31")))
        365

        Generator properties:
        >>> gen = date_range("2025-12-01", "2025-12-03")
        >>> next(gen)
        '2025-12-01'
        >>> list(gen)  # consumes remaining items
        ['2025-12-02', '2025-12-03']
    """
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)

    return (
        (start + timedelta(days=n)).isoformat() for n in range((end - start).days + 1)
    )


class DateRange:
    """
    Iterator class for date ranges between start_date (inclusive) and end_date (inclusive)

    Examples:
        >>> dr = DateRange("2025-12-01", "2025-12-05")

        Length:
        >>> len(DateRange("2025-12-01", "2025-12-10"))
        10

        Basic iteration:
        >>> list(dr)
        ['2025-12-01', '2025-12-02', '2025-12-03', '2025-12-04', '2025-12-05']
        >>> for d in dr:
        ...    print(d)
        2025-12-01
        2025-12-02
        2025-12-03
        2025-12-04
        2025-12-05
        >>> for d in reversed(dr):
        ...    print(d)
        2025-12-05
        2025-12-04
        2025-12-03
        2025-12-02
        2025-12-01


        Slicing:
        >>> dr[:3]
        ['2025-12-01', '2025-12-02', '2025-12-03']
        >>> dr[1:2]
        ['2025-12-02']

        Membership testing:
        >>> "2025-12-02" in dr
        True
        >>> "2025-12-06" in dr
        False

        Randomized pick
        >>> import random
        >>> random.seed(10)
        >>> random.choice(dr)
        '2025-12-05'


    """

    def __init__(self, start_date: str, end_date: str):
        self.start = date.fromisoformat(start_date)
        self.end = date.fromisoformat(end_date)

        if self.start > self.end:
            raise ValueError(
                f"start_date ({start_date}) must be <= end_date ({end_date})"
            )
        self._dates = [
            (self.start + timedelta(days=n)).isoformat()
            for n in range((self.end - self.start).days + 1)
        ]

    def __len__(self) -> int:
        return (self.end - self.start).days + 1

    def __getitem__(self, index: int) -> str:
        return self._dates[index]
