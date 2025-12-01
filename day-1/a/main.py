from dataclasses import dataclass


@dataclass
class Line:
    direction: str
    clicks: int

    @classmethod
    def parse(cls, line: str):
        return cls(direction=line[0], clicks=int(line[1:]))


def solve(lines: list[Line]):
    current = 50
    result = 0
    for line in lines:
        current += line.clicks * (-1 if line.direction == 'L' else 1)
        current = current % 100
        result += int(current == 0)
    return result
