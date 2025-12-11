from .common import Server, get_number_paths


def solve(servers: list[Server]):
    server_map = {server.name: server for server in servers}
    return get_number_paths('you', 'out', server_map)
