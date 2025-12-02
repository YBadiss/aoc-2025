from typing import Callable
from dataclasses import dataclass
import importlib


@dataclass
class DayModule:
    day: str

    def test(self) -> str:
        data = self._get_data(f'{self._day_part}.data.test')
        data, expected_result = [self._parser(d) for d in data[:-1]], data[-1]
        actual_result = str(self._solver(data))
        if actual_result != expected_result:
            raise ValueError(f'Expected {expected_result} but got {actual_result}')
        return actual_result
    
    def run(self) -> str:
        data = self._get_data('data')
        data = [self._parser(d) for d in data]
        result = str(self._solver(data))
        return result
    
    @property
    def _day_number(self) -> str:
        return self.day[:-1]
    
    @property
    def _day_part(self) -> str:
        return self.day[-1]
    
    @property
    def _folder_path(self) -> str:
        return f'day-{self._day_number}'
    
    @property
    def _module_path(self) -> str:
        return self._folder_path.replace('/', '.')

    @property
    def _py_module(self):
        return importlib.import_module(self._module_path)
    
    @property
    def _parser(self) -> Callable:
        return self._py_module.parser
    
    @property
    def _solver(self) -> Callable:
        return getattr(self._py_module, f'solver_{self._day_part}')
    
    @property
    def _delimiter(self) -> str:
        return self._py_module.delimiter

    def _get_data(self, data_file: str) -> list[str]:
        with open(f'{self._folder_path}/{data_file}', 'r') as f:
            data = f.read().split(self._delimiter)
            return data
