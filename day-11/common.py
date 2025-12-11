from dataclasses import dataclass


@dataclass
class Server:
    name: str
    outputs: list[str]

    @classmethod
    def parse(cls, line: str) -> 'Server':
        name, outputs = line.split(': ')
        return cls(name=name, outputs=outputs.split(' '))


def get_number_paths(start: str, end: str, server_map: dict[str, Server]) -> int:
    num_paths = {end: 1}
    def _get_number_paths(start: str, end: str, server_map: dict[str, Server]) -> int:
        if start in num_paths:
            return num_paths[start]
        if start not in server_map:
            return 0
        total_paths = 0
        for next_server in server_map[start].outputs:
            num_paths[next_server] = _get_number_paths(next_server, end, server_map)
            total_paths += num_paths[next_server]
        return total_paths
    return _get_number_paths(start, end, server_map)


parser = Server.parse
delimiter = '\n'
