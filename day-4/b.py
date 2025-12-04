from .common import GridRow, pick_up_rolls


def solve(grid: list[GridRow]):
    total_picked_up_rolls = 0
    picked_up_rolls = set()
    while True:
        rolls_to_pick_up = pick_up_rolls(grid, picked_up_rolls)
        if rolls_to_pick_up:
            total_picked_up_rolls += len(rolls_to_pick_up)
            picked_up_rolls = picked_up_rolls.union(rolls_to_pick_up)
        else:
            return total_picked_up_rolls
