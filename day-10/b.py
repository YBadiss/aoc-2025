from .common import Machine
from typing import cast
import z3


def solve(machines: list[Machine]):
    total_button_press = 0
    for machine in machines:
        total_button_press += min_button_presses_z3(machine)
    return total_button_press


def min_button_presses_z3(machine: Machine) -> int:
    # Universe of jolts (all indices we care about)
    jolt_indexes = list(range(len(machine.joltage.levels)))
    # Decision vars: press[j] in N, number of presses
    button_presses = [z3.Int(f"press_{i}") for i in range(len(machine.buttons))]
    
    opt = z3.Optimize()
    # Constrain press vars to be >= 0
    for button_press in button_presses:
        opt.add(button_press >= 0)
    # For each jolt, compute its value as the sum of button presses
    for jolt_index in jolt_indexes:
        jolt_button_presses = [
            button_presses[j]
            for j, b in enumerate(machine.buttons)
            if jolt_index in b.indexes
        ]
        final_state = z3.Sum(*jolt_button_presses) if jolt_button_presses else 0
        target_state = machine.joltage.levels[jolt_index]
        opt.add(final_state == target_state)

    # Objective: minimize number of presses
    total_presses = z3.Sum(*button_presses) if button_presses else 0
    opt.minimize(total_presses)
    # Solve
    if opt.check() != z3.sat:
        raise ValueError('Cant solve')
    
    model = opt.model()
    min_count = sum(
        cast(z3.IntNumRef, model.eval(button_press)).as_long()
        for button_press in button_presses
    )
    return min_count
