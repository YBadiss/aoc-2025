from .common import IngredientId, IngredientIdRange, merge_ranges


def solve(input_list: list[IngredientId | IngredientIdRange | None]):
    ingredient_id_ranges = [r for r in input_list if isinstance(r, IngredientIdRange)]
    merged_ranges = merge_ranges(ingredient_id_ranges)
    
    num_of_fresh_ingredients = 0
    ingredient_ids = [i for i in input_list if isinstance(i, IngredientId)]
    for ingredient_id in ingredient_ids:
        found_range = _binary_search_range(ingredient_id, merged_ranges, 0, len(merged_ranges) - 1)
        if found_range:
            num_of_fresh_ingredients += 1
    return num_of_fresh_ingredients


def _binary_search_range(
    ingredient_id: IngredientId,
    merged_ranges: list[IngredientIdRange],
    start: int,
    end: int
) -> IngredientIdRange | None:
    if end < start:
        return None
    elif end == start:
        if ingredient_id.id_ >= merged_ranges[start].start and ingredient_id.id_ <= merged_ranges[start].end:
            return merged_ranges[start]
        else:
            return None
    mid = (end + start + 1) // 2
    if ingredient_id.id_ < merged_ranges[mid].start:
        return _binary_search_range(ingredient_id, merged_ranges, start, mid - 1)
    elif ingredient_id.id_ > merged_ranges[mid].start:
        return _binary_search_range(ingredient_id, merged_ranges, mid, end)
    else:
        return merged_ranges[mid]