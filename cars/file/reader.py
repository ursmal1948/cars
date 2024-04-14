import json
from abc import ABC, abstractmethod
from typing import Any


class FileService(ABC):

    @abstractmethod
    def get_lines(self, path: str, key: str = None) -> list[dict[str, Any]]:
        pass


class JsonFileService(FileService):
    SUPPORTED_EXTENSIONS = '.json'

    def get_lines(self, path: str, key: str = None) -> list[dict[str, Any]]:
        if not path.endswith(JsonFileService.SUPPORTED_EXTENSIONS):
            raise AttributeError('File has incorrect extension')
        try:
            with open(path, 'r') as json_file:
                data_from_file = json.load(json_file)
        except Exception as e:
            raise FileNotFoundError(f'File not found: {e}')
        if key not in data_from_file:
            raise AttributeError(f'Key not found: {key}')
        return data_from_file[key]


class TxtFileService(FileService):
    SUPPORTED_EXTENSIONS = '.txt'

    def get_lines(self, path: str, key: str = None) -> list[dict[str, Any]]:
        cars_data = []
        if not path.endswith(TxtFileService.SUPPORTED_EXTENSIONS):
            raise AttributeError(f'File has incorrect extension: {path[-3:]}')
        try:
            with open(path, 'r') as f:
                lines = [line.strip() if line.endswith('\n') else line for line in f.readlines()]

                for line in lines:
                    try:
                        car_data = line.split(',')
                        car = {
                            'model': car_data[0],
                            'price': int(car_data[1]),
                            'color': car_data[2],
                            'mileage': int(car_data[3]),
                            'components': car_data[4].split(':') if len(car_data[4]) > 0 else []
                        }
                        cars_data.append(car)
                    except ValueError:
                        raise ValueError(f'Error parsing line: {line}')
                return cars_data
        except FileNotFoundError as fe:
            raise FileNotFoundError(f'File not found: {fe}')
