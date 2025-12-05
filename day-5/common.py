from dataclasses import dataclass


@dataclass
class IngredientIdRange:
    start: int
    end: int

    @classmethod
    def parse(cls, line: str) -> 'IngredientIdRange':
        start, end = line.split('-')
        return cls(start=int(start), end=int(end))
    

@dataclass
class IngredientId:
    id_: int

    @classmethod
    def parse(cls, line: str) -> 'IngredientId':
        return cls(id_=int(line))


def merge_ranges(ingredient_id_ranges: list[IngredientIdRange]) -> list[IngredientIdRange]:
    ingredient_id_ranges.sort(key=lambda r: (r.start, r.end))
    merged_ranges = []
    start, end = ingredient_id_ranges[0].start, ingredient_id_ranges[0].end
    for i in range(1, len(ingredient_id_ranges)):
        if ingredient_id_ranges[i].start <= end:
            end = max(end, ingredient_id_ranges[i].end)
        else:
            merged_ranges.append(IngredientIdRange(start, end))
            start, end = ingredient_id_ranges[i].start, ingredient_id_ranges[i].end
    merged_ranges.append(IngredientIdRange(start, end))
    return merged_ranges

    

def parser(line: str):
    if not line:
        return None
    if '-' in line:
        return IngredientIdRange.parse(line)
    else:
        return IngredientId.parse(line)


delimiter = '\n'
