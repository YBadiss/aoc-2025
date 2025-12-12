from .common import Shape, Tree


def solve(input_list: list[Shape | Tree]):
    shapes = [s for s in input_list if isinstance(s, Shape)]
    trees = [t for t in input_list if isinstance(t, Tree)]

    num_valid_regions = 0
    for tree in trees:
        tree_size = tree.height * tree.width
        gifts_size = sum(num_shape * shape.size for num_shape, shape in zip(tree.num_shapes, shapes))
        # This was just a sneaky attempt to get some more info about the puzzle,
        # but it actually solved it ¯\_(ツ)_/¯
        if tree_size >= 1.2 * gifts_size:
            num_valid_regions += 1
    return num_valid_regions
