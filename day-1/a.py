from .common import Rotation


def solve(rotations: list[Rotation]):
    current_position = 50
    zero_count = 0
    for rotation in rotations:
        current_position += rotation.clicks * (-1 if rotation.direction == 'L' else 1)
        current_position = current_position % 100
        zero_count += int(current_position == 0)
    return zero_count
