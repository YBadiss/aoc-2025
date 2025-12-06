from dataclasses import dataclass
import math
from typing import Callable, Iterator


@dataclass
class OperandsRow:
    operands: list[int]
    line: str

    @classmethod
    def parse(cls, line: str) -> 'OperandsRow':
        operands = [int(op) for op in line.split(' ') if op != '']
        return cls(operands=operands, line=line)
    

@dataclass
class OperatorsRow:
    operators: list[str]

    @classmethod
    def parse(cls, line: str) -> 'OperatorsRow':
        operators = [op for op in line.split(' ') if op != '']
        return cls(operators=operators)


OPERATIONS = {
    '+': sum,
    '*': math.prod
}


def parser(line: str):
    if any(operator in line for operator in OPERATIONS.keys()):
        return OperatorsRow.parse(line)
    else:
        return OperandsRow.parse(line)
    

def common_solve(ops: list[OperandsRow | OperatorsRow], get_operands: Callable[[list[OperandsRow]], Iterator[list[int]]]):
    operands_rows = [op for op in ops if isinstance(op, OperandsRow)]
    operators_row = next(op for op in ops if isinstance(op, OperatorsRow))
    total = 0
    for i, operands in enumerate(get_operands(operands_rows)):
        operator = operators_row.operators[i]
        total += OPERATIONS[operator](operands)
    return total


delimiter = '\n'
