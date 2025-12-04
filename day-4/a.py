from .common import GridRow, pick_up_rolls


def solve(grid: list[GridRow]):
    rolls_to_pick_up = pick_up_rolls(grid, set())
    return len(rolls_to_pick_up)
