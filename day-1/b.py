from .common import Rotation


def solve(rotations: list[Rotation]):
    current_position = 50
    zero_count = 0
    for rotation in rotations:
        # move the position
        temp_position = current_position + rotation.clicks * (-1 if rotation.direction == 'L' else 1)
        # if we are exactly at 0, we have passed 0 only once
        if temp_position == 0:
            zero_passes = 1
        else:
            # otherwise, count the number of hundreds we've passed through
            zero_passes = abs(temp_position) // 100
            # and add one if we have crossed 0
            if temp_position < 0 and current_position > 0:
                zero_passes += 1
        zero_count += zero_passes
        current_position = temp_position % 100
    return zero_count
