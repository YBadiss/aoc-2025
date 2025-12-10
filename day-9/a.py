from .common import TilePosition, compute_area
import itertools


def solve(red_tile_positions: list[TilePosition]):
    max_area = 0
    for p1, p2 in itertools.combinations(red_tile_positions, 2):
        max_area = max(compute_area(p1, p2), max_area)
    return max_area
