from .common import ManifoldRow
from collections import defaultdict


def solve(manifold: list[ManifoldRow]):
    starting_position = manifold[0].start
    if starting_position is None:
        raise ValueError('There must be a starting position in the first row')
    beam_paths = _get_beam_paths(starting_x=starting_position, manifold=manifold[1:])
    # Return the sum of the beams that reached each final x index
    return sum(beam_paths.values())


def _get_beam_paths(starting_x: int, manifold: list[ManifoldRow]) -> dict[int,int]:
    beams_x = defaultdict(int)
    beams_x[starting_x] = 1
    for beam_y in range(len(manifold)):
        # Compute beams that split
        beams_x_set = set(beams_x.keys())
        split_beams_x = beams_x_set.intersection(manifold[beam_y].splitters)
        for split_beam_x in split_beams_x:
            # Keep the weight of each x index (number of beams going through it)
            # and pass it down to children beams
            beams_x[split_beam_x - 1] += beams_x[split_beam_x]
            beams_x[split_beam_x + 1] += beams_x[split_beam_x]
            # Reset the main beam to 0 as it has stopped
            beams_x[split_beam_x] = 0
    # Return the final number of beams for each x index
    return beams_x
