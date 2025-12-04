from .common import Bank, solve as solve_common


def solve(banks: list[Bank]):
    return solve_common(banks, 2)
