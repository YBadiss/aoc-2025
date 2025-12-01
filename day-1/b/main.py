from dataclasses import dataclass


@dataclass
class Line:
    direction: str
    clicks: int

    @classmethod
    def parse(cls, line: str):
        return cls(direction=line[0], clicks=int(line[1:]))


def solve(lines: list[Line]):
    pos = 50
    result = 0
    for line in lines:
        # move the position
        temp_pos = pos + line.clicks * (-1 if line.direction == 'L' else 1)
        # if we are exactly at 0, we have passed 0 only once
        if temp_pos == 0:
            zero_passes = 1
        else:
            # otherwise, count the number of hundreds we've passed through
            zero_passes = abs(temp_pos) // 100
            # and add one if we have crossed 0
            if temp_pos < 0 and pos > 0:
                zero_passes += 1
        result += zero_passes
        pos = temp_pos % 100
    return result
