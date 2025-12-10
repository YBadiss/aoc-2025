from .common import Machine
import z3


def solve(machines: list[Machine]):
    total_button_press = 0
    for machine in machines:
        total_button_press += min_button_presses_z3(machine)
    return total_button_press


def min_button_presses_z3(machine: Machine) -> int:
    # Universe of lights (all indices we care about)
    light_indexes = machine.lights.on | machine.lights.off
    # Decision vars: press[j] in {True, False}
    button_presses = [z3.Bool(f"press_{j}") for j in range(len(machine.buttons))]

    opt = z3.Optimize()
    # For each light i, compute parity of presses of buttons that toggle it
    for light_index in light_indexes:
        toggles = [
            z3.If(button_presses[j], 1, 0)
            for j, b in enumerate(machine.buttons)
            if light_index in b.indexes
        ]
        final_state = z3.Sum(*toggles) % 2 if toggles else 0
        target_state = 1 if light_index in machine.lights.on else 0
        opt.add(final_state == target_state)

    # Objective: minimize number of presses
    total_presses = z3.Sum(*button_presses) if button_presses else 0
    opt.minimize(total_presses)
    # Solve
    if opt.check() != z3.sat:
        raise ValueError('Cant solve')

    model = opt.model()
    pressed = [j for j, pj in enumerate(button_presses) if z3.is_true(model.eval(pj))]
    min_count = len(pressed)
    return min_count
