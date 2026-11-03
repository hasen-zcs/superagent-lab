"""Tests for calc.py. Run: python3 test_calc.py"""
from calc import moving_average, is_even, clamp

failures = []


def check(name, got, want):
    if got != want:
        failures.append(f"{name}: got {got!r}, want {want!r}")
    else:
        print(f"ok {name}")


check("moving_average [1,2,3,4]", moving_average([1, 2, 3, 4]), 2.5)
check("moving_average [10]", moving_average([10]), 10.0)
check("moving_average negatives", moving_average([-2, 2]), 0.0)
check("is_even 4", is_even(4), True)
check("is_even 7", is_even(7), False)
check("clamp inside", clamp(5, 0, 10), 5)
check("clamp below", clamp(-1, 0, 10), 0)
check("clamp above", clamp(99, 0, 10), 10)

if failures:
    print("\nFAILED:")
    for f in failures:
        print(" -", f)
    raise SystemExit(1)
print("\nall tests passed")
