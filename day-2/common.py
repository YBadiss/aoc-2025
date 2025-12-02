from dataclasses import dataclass


@dataclass
class IdRange:
    start: int
    end: int

    @classmethod
    def parse(cls, line: str) -> 'IdRange':
        start, end = line.split('-')
        return cls(start=int(start), end=int(end))


parser = IdRange.parse
delimiter = ','
