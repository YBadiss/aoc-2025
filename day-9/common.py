from dataclasses import dataclass


@dataclass
class TilePosition:
    x: int
    y: int

    @classmethod
    def parse(cls, line: str) -> 'TilePosition':
        x, y = line.split(',')
        return cls(x=int(x), y=int(y))


def compute_area(p1: TilePosition, p2: TilePosition) -> int:
    return (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)


parser = TilePosition.parse
delimiter = '\n'
