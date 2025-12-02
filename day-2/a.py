from .common import IdRange


def solve(id_ranges: list[IdRange]):
    sum_of_repeated_patterns = 0
    for id_range in id_ranges:
        for i in range(id_range.start, id_range.end + 1):
            id_ = str(i)
            if id_[:len(id_) // 2] == id_[len(id_) // 2:]:
                sum_of_repeated_patterns += i
    return sum_of_repeated_patterns
