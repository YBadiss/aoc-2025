from dataclasses import dataclass


@dataclass
class Rotation:
    direction: str
    clicks: int

    @classmethod
    def parse(cls, line: str) -> 'Rotation':
        return cls(direction=line[0], clicks=int(line[1:]))


parser = Rotation.parse
delimiter = '\n'
