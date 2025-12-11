from .common import Server, get_number_paths


def solve(servers: list[Server]):
    server_map = {server.name: server for server in servers}
    # svr -> dac -> fft -> out
    svr_to_dac = get_number_paths('svr', 'dac', server_map)
    dac_to_fft = get_number_paths('dac', 'fft', server_map)
    fft_to_out = get_number_paths('fft', 'out', server_map)
    # svr -> fft -> dac -> out
    svr_to_fft = get_number_paths('svr', 'fft', server_map)
    fft_to_dac = get_number_paths('fft', 'dac', server_map)
    dac_to_out = get_number_paths('dac', 'out', server_map)
    # total paths
    return (svr_to_fft * fft_to_dac * dac_to_out) + (svr_to_dac * dac_to_fft * fft_to_out)
