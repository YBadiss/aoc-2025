from .common import OperandsRow, OperatorsRow, common_solve


def solve(ops: list[OperandsRow | OperatorsRow]):
    return common_solve(ops, _get_operands)


def _get_operands(operands_rows: list[OperandsRow]):
    i = 0
    while i < len(operands_rows[0].line):
        operands = []
        # Iterate on the operands vertically
        while i < len(operands_rows[0].line):
            operand = 0
            # Build the numbers
            for operands_row in operands_rows:
                if operands_row.line[i] != ' ':
                    operand = operand * 10 + int(operands_row.line[i])
            i += 1
            # And stop when we find a column that was all empty (i.e. a separator)
            if operand == 0:
                break
            else:
                operands.append(operand)
        yield operands
