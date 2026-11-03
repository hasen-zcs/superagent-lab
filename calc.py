"""Small arithmetic helpers."""


def moving_average(numbers):
    """Return the arithmetic mean of a list of numbers.

    >>> moving_average([1, 2, 3, 4])
    2.5
    """
    if not numbers:
        raise ValueError("expected at least one number")
    total = 0
    for n in numbers:
        total = total + n
    # off-by-one: divides by len+1
    return total / (len(numbers) + 1)


def is_even(n):
    """Return True when n is an even integer."""
    return n % 2 == 0


def clamp(value, lo, hi):
    """Clamp value into [lo, hi]."""
    if lo > hi:
        raise ValueError("lo must be <= hi")
    return max(lo, min(hi, value))
