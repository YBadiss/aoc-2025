from .common import IdRange


def solve(id_ranges: list[IdRange]):
    sum_of_repeated_patterns = 0
    for id_range in id_ranges:
        for i in range(id_range.start, id_range.end + 1):
            if _is_anomaly(str(i)):
                sum_of_repeated_patterns += i
    return sum_of_repeated_patterns


def _is_anomaly(s: str) -> bool:
    for i in range(len(s) // 2):
        if _is_made_of_pattern(s, s[0:i+1]):
            return True
    return False


def _is_made_of_pattern(s: str, pattern: str) -> bool:
    i = 0
    pattern_len = len(pattern)
    while i < len(s):
        if s[i:i+pattern_len] != pattern:
            return False
        i += pattern_len
    return True
