from .common import IngredientId, IngredientIdRange, merge_ranges


def solve(input_list: list[IngredientId | IngredientIdRange | None]):
    ingredient_id_ranges = [r for r in input_list if isinstance(r, IngredientIdRange)]
    merged_ranges = merge_ranges(ingredient_id_ranges)
    
    num_of_fresh_ingredients = sum(
        len(range(ingredient_id_range.start, ingredient_id_range.end + 1))
        for ingredient_id_range in merged_ranges
    )
    return num_of_fresh_ingredients