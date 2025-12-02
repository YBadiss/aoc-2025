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
            if _is_anomaly(str(i)):
                result += i
    return result


def _is_anomaly(s: str) -> bool:
    for i in range(len(s) // 2):
        if _is_made_of_pattern(s, s[0:i+1]):
            return True
    return False


def _is_made_of_pattern(s: str, pattern: str) -> bool:
    i = 0
    l = len(pattern)
    while i < len(s):
        if s[i:i+l] != pattern:
            return False
        i += l
    return True
