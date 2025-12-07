from .common import ManifoldRow


def solve(manifold: list[ManifoldRow]):
    starting_position = manifold[0].start
    if starting_position is None:
        raise ValueError('There must be a starting position in the first row')
    active_splitters = _get_active_splitters(starting_x=starting_position, manifold=manifold[1:])
    return len(active_splitters)


def _get_active_splitters(starting_x: int, manifold: list[ManifoldRow]) -> set[tuple[int,int]]:
    beams_x = {starting_x}
    active_splitters = set()
    for beam_y in range(len(manifold)):
        # Compute beams that split and those that go on straight ahead
        split_beams_x = beams_x.intersection(manifold[beam_y].splitters)
        straight_beams_x = beams_x.difference(manifold[beam_y].splitters)
        # Add new splitters (x,y) positions to the set of active splitters
        active_splitters = active_splitters.union({(split_beam_x, beam_y) for split_beam_x in split_beams_x})
        # Compute the new created beams
        new_beams_x = set()
        for split_beam_x in split_beams_x:
            new_beams_x.add(split_beam_x - 1)
            new_beams_x.add(split_beam_x + 1)
        # Combine new beams and those that went on straight to get the new set of beams
        beams_x = straight_beams_x.union(new_beams_x)
    return active_splitters
