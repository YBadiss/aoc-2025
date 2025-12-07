from dataclasses import dataclass


@dataclass
class ManifoldRow:
    start: int | None
    splitters: set[int]

    @classmethod
    def parse(cls, line: str) -> 'ManifoldRow':
        start = next((i for i in range(len(line)) if line[i] == 'S'), None)
        splitters = {i for i in range(len(line)) if line[i] == '^'}
        return cls(start=start, splitters=splitters)


parser = ManifoldRow.parse
delimiter = '\n'
