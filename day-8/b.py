from .common import JunctionBoxPosition, get_shortest_connection, combine_circuits


def solve(input_list: list[JunctionBoxPosition]):
    junction_box_positions = [p for p in input_list if isinstance(p, JunctionBoxPosition)]
    circuits = []
    for box_a, box_b in get_shortest_connection(junction_box_positions):
        circuits = combine_circuits(circuits, box_a, box_b)
        if len(circuits) == 1 and len(circuits[0]) == len(junction_box_positions):
            # Once we have a single circuit containing all boxes, return the result
            return junction_box_positions[box_a].x * junction_box_positions[box_b].x
