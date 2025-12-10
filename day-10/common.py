from dataclasses import dataclass


@dataclass
class Lights:
    on: set[int]
    off: set[int]

    @classmethod
    def parse(cls, line: str) -> 'Lights':
        on = {i for i, s in enumerate(line) if s == '#'}
        off = {i for i, s in enumerate(line) if s == '.'}
        return cls(on=on, off=off)
    
    def toggle(self, light_idxs: set[int]) -> 'Lights':
        to_on = light_idxs.difference(self.on)
        to_off = light_idxs.difference(self.off)
        on = self.on.difference(to_off).union(to_on)
        off = self.off.difference(to_on).union(to_off)
        return Lights(on=on, off=off)
    
    def turn_off(self) -> 'Lights':
        on = set()
        off = self.off.union(self.on)
        return Lights(on=on, off=off)
    
    def diff(self, other: 'Lights') -> set[int]:
        return self.on.difference(other.on).union(self.off.difference(other.off))


@dataclass
class Button:
    indexes: set[int]

    @classmethod
    def parse(cls, line: str) -> 'Button':
        indexes = {int(s) for s in line.split(',')}
        return cls(indexes=indexes)


@dataclass
class Joltage:
    levels: list[int]

    @classmethod
    def parse(cls, line: str) -> 'Joltage':
        levels = [int(s) for s in line.split(',')]
        return cls(levels=levels)
    
    def increase(self, level_idxs: set[int]) -> 'Joltage':
        levels = [level + int(i in level_idxs) for i, level in enumerate(self.levels)]
        return Joltage(levels=levels)
    
    def turn_off(self) -> 'Joltage':
        levels = [0 for _ in self.levels]
        return Joltage(levels=levels)
    
    def diff(self, other: 'Joltage') -> set[int]:
        return {
            i
            for i in range(len(self.levels))
            if self.levels[i] != other.levels[i]
        }


@dataclass
class Machine:
    lights: Lights
    buttons: list[Button]
    joltage: Joltage

    @classmethod
    def parse(cls, line: str) -> 'Machine':
        machine_parts = line.split(' ')
        lights = Lights.parse(machine_parts[0][1:-1])
        joltage = Joltage.parse(machine_parts[-1][1:-1])
        buttons = [Button.parse(s[1:-1]) for s in machine_parts[1:-1]]
        return cls(lights=lights, buttons=buttons, joltage=joltage)


parser = Machine.parse
delimiter = '\n'
