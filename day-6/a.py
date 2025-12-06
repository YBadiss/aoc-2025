from .common import OperandsRow, OperatorsRow, common_solve


def solve(ops: list[OperandsRow | OperatorsRow]):
    return common_solve(ops, _get_operands)


def _get_operands(operands_rows: list[OperandsRow]):
    for i in range(len(operands_rows[0].operands)):
        yield [operands_row.operands[i] for operands_row in operands_rows]
