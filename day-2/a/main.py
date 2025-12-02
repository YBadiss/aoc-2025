from dataclasses import dataclass


@dataclass
class Line:
    start: int
    end: int

    @classmethod
    def parse(cls, line: str):
        start, end = line.split('-')
        return cls(start=int(start), end=int(end))


def solve(lines: list[Line]):
    result = 0
    for line in lines:
        for i in range(line.start, line.end + 1):
            id_ = str(i)
            if id_[:len(id_) // 2] == id_[len(id_) // 2:]:
                result += i
    return result
