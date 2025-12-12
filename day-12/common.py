from dataclasses import dataclass


@dataclass
class Shape:
    index: int
    lines: list[str]

    @property
    def size(self) -> int:
        return sum(
            1 if cell == '#' else 0
            for line in self.lines
            for cell in line
        )


@dataclass
class Tree:
    width: int
    height: int
    num_shapes: list[int]

    @classmethod
    def parse(cls, line: str) -> 'Tree':
        dimensions, num_shapes = line.split(': ')
        width, height = dimensions.split('x')
        num_shapes = num_shapes.split(' ')
        return Tree(
            width=int(width),
            height=int(height),
            num_shapes=[int(n) for n in num_shapes],
        )


def make_parser():
    shapes = [[]]
    def _parser(line: str) -> Shape | Tree | None:
        if '#' in line:
            shapes[-1].append(line)
            return None
        elif 'x' in line:
            # tree line
            return Tree.parse(line)
        elif ':' in line:
            # shape index, skip
            return None
        else:
            # empty line, end of shape
            shape = Shape(index=len(shapes) - 1, lines=[s for s in shapes[-1]])
            shapes.append([])
            return shape
    return _parser
    

parser = make_parser()
delimiter = '\n'
