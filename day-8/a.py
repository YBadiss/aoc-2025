from .common import JunctionBoxPosition, get_shortest_connection, combine_circuits
import heapq
import math


def solve(input_list: list[JunctionBoxPosition | int]):
    number_of_connections = next(v for v in input_list if isinstance(v, int))
    junction_box_positions = [p for p in input_list if isinstance(p, JunctionBoxPosition)]
    circuits = []
    for i, (box_a, box_b) in enumerate(get_shortest_connection(junction_box_positions)):
        if i >= number_of_connections:
            circuit_sizes = []
            for circuit in circuits:
                heapq.heappush(circuit_sizes, len(circuit))
            return math.prod(heapq.nlargest(3, circuit_sizes))
        circuits = combine_circuits(circuits, box_a, box_b)

