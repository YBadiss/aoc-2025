from dataclasses import dataclass
import math
import heapq
from typing import Iterable


@dataclass
class JunctionBoxPosition:
    x: int
    y: int
    z: int

    @classmethod
    def parse(cls, line: str) -> 'JunctionBoxPosition':
        x, y, z = line.split(',')
        return cls(x=int(x), y=int(y), z=int(z))


def get_shortest_connection(junction_box_positions: list[JunctionBoxPosition]) -> Iterable[tuple[int, int]]:
    boxes_by_distance = _order_boxes_by_distance(junction_box_positions)
    while boxes_by_distance:
        yield heapq.heappop(boxes_by_distance)[1]
    raise StopIteration()


def combine_circuits(circuits: list[set[int]], box_a: int, box_b: int) -> list[set[int]]:
    """
    Build a new list of circuits once boxes A and B have been connected
    """
    # Start with an empty list of new circuits
    new_circuits = []
    # and a combined circuit of just A and B (our new link).
    combined_circuit = {box_a, box_b}
    for circuit in circuits:
        if box_a in circuit or box_b in circuit:
            # If the circuit contains either A or B add it to the fully combined circuit,
            # and effectively remove the old circuit from the new list.
            combined_circuit = combined_circuit.union(circuit)
        else:
            # Otherwise just add that circuit as is to the new list of circuits.
            new_circuits.append(circuit)
    return new_circuits + [combined_circuit]
    

def _order_boxes_by_distance(junction_box_positions: list[JunctionBoxPosition]) -> list[tuple[int, tuple[int, int]]]:
    """
    Build a heap of distances between all boxes
    """
    boxes_by_distances = []
    for box_i in range(len(junction_box_positions)):
        for box_j in range(box_i + 1, len(junction_box_positions)):
            d = math.sqrt(
                pow(junction_box_positions[box_i].x - junction_box_positions[box_j].x, 2)
                + pow(junction_box_positions[box_i].y - junction_box_positions[box_j].y, 2)
                + pow(junction_box_positions[box_i].z - junction_box_positions[box_j].z, 2)
            )
            heapq.heappush(boxes_by_distances, (d, (box_i, box_j)))
    return boxes_by_distances


def parser(line: str) -> JunctionBoxPosition | int:
    if ',' in line:
        return JunctionBoxPosition.parse(line)
    else:
        return int(line)


delimiter = '\n'
