from typing import Callable
from dataclasses import dataclass
import importlib


@dataclass
class DayModule:
    day: str

    def test(self) -> str:
        lines = self._get_lines('data.test')
        data, expected_result = [self._parser(line) for line in lines[:-1]], lines[-1]
        actual_result = str(self._solver(data))
        if actual_result != expected_result:
            raise ValueError(f'Expected {expected_result} but got {actual_result}')
        return actual_result
    
    def run(self) -> str:
        lines = self._get_lines('data')
        data = [self._parser(line) for line in lines[:-1]]
        result = str(self._solver(data))
        return result
    
    @property
    def _parser(self) -> Callable:
        return self._py_module.Line.parse
    
    @property
    def _solver(self) -> Callable:
        return self._py_module.solve

    @property
    def _py_module(self):
        return importlib.import_module(f'{self._module_path}.main')
    
    @property
    def _folder_path(self) -> str:
        day_number = self.day[:-1]
        day_step = self.day[-1]
        return f'day-{day_number}/{day_step}'
    
    @property
    def _module_path(self) -> str:
        return self._folder_path.replace('/', '.')

    def _get_lines(self, data_file: str) -> list[str]:
        with open(f'{self._folder_path}/{data_file}', 'r') as f:
            return f.read().splitlines()
