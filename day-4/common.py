from dataclasses import dataclass


@dataclass
class GridRow:
    cells: list[str]

    @classmethod
    def parse(cls, line: str) -> 'GridRow':
        return cls(cells=list(line))


def pick_up_rolls(grid: list[GridRow], picked_up_rolls: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """
    Go through the grid and find all the rolls that can be picked up.
    Build up a set of positions to return.
    """
    rolls_to_pick_up = set()
    for i in range(len(grid)):
        for j in range(len(grid[i].cells)):
            if _is_roll(i, j, grid, picked_up_rolls) and _is_accessible(i, j, grid, picked_up_rolls):
                rolls_to_pick_up.add((i, j))
    return rolls_to_pick_up


def _is_accessible(i: int, j: int, grid: list[GridRow], picked_up_rolls: set[tuple[int, int]]) -> bool:
    """
    Check if the cell at (i, j) can be picked up by counting the surrounding rolls.
    """
    roll_count = 0
    for i_chg in (-1, 0, 1):
        for j_chg in (-1, 0, 1):
            if i_chg == 0 and j_chg == 0:
                continue
            roll_count += int(_is_roll(i + i_chg, j + j_chg, grid, picked_up_rolls))
    return roll_count < 4

    
def _is_roll(i: int, j: int, grid: list[GridRow], picked_up_rolls: set[tuple[int, int]]) -> bool:
    """
    Check if a cell contains a roll.
    - positions outside the grid have no rolls
    - rolls already picked up are no longer considered
    """
    if i < 0 or i >= len(grid):
        return False
    elif j < 0 or j >= len(grid[i].cells):
        return False
    return ((i, j) not in picked_up_rolls) and grid[i].cells[j] == '@'


parser = GridRow.parse
delimiter = '\n'
