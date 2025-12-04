from dataclasses import dataclass


@dataclass
class Bank:
    batteries: list[int]

    @classmethod
    def parse(cls, line: str) -> 'Bank':
        batteries = [int(c) for c in line]
        return cls(batteries=batteries)
    

def solve(banks: list[Bank], number_digits: int):
    total_joltage = 0
    for bank in banks:
        start = 0
        battery_joltage = 0
        # Iterate over the number of digits in reverse, to ensure whatever
        # max value we find still has enough batteries behind it to compose
        # the final joltage value for this bank.
        for i in range(number_digits - 1, -1, -1):
            end = len(bank.batteries) - i
            # Find the max between `start` and `end` and then update `start`
            # and `battery_joltage`
            digit, position = _find_next_digit(bank.batteries[start:end])
            start += position + 1
            battery_joltage = battery_joltage * 10 + digit
        total_joltage += battery_joltage
    return str(total_joltage)


def _find_next_digit(batteries: list[int]) -> tuple[int, int]:
    """
    Given a list of battery joltage, find the max voltage and its position.
    """
    max_i = -1
    max_battery = -1
    for i, battery in enumerate(batteries):
        if battery > max_battery:
            max_battery = battery
            max_i = i
    return max_battery, max_i


parser = Bank.parse
delimiter = '\n'
