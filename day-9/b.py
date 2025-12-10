from .common import TilePosition, compute_area
import itertools


def solve(red_tile_positions: list[TilePosition]):
    max_area = 0
    for p1, p2 in itertools.combinations(red_tile_positions, 2):
        area = compute_area(p1, p2)
        if area >= max_area and is_polygon_contained(p1, p2, red_tile_positions):
            max_area = area
    return max_area


def is_polygon_contained(p1: TilePosition, p2: TilePosition, red_tile_positions: list[TilePosition]) -> bool:
    # To test if an axis-aligned line segment intersects an axis-aligned box,
    # we just check to see if the line segment falls
    # completely to the left of the left side of the box,
    # completely to the right of the right side of it,
    # completely above the top of it,
    # or completely below the bottom of it.
    # If not, then it intersects.
    
    min_x, max_x = min(p1.x, p2.x), max(p1.x, p2.x)
    min_y, max_y = min(p1.y, p2.y), max(p1.y, p2.y)

    for p3, p4 in itertools.pairwise(red_tile_positions):
        if not (
            max(p3.x, p4.x) <= min_x  # is_to_the_left
            or min(p3.x, p4.x) >= max_x  # is_to_the_right
            or max(p3.y, p4.y) <= min_y  # is_to_the_bottom
            or min(p3.y, p4.y) >= max_y  # is_to_the_top
        ):
            return False
    return True
