import json
from abc import ABC, abstractmethod
from typing import Any
import aiofiles


class FileService(ABC):
    @abstractmethod
    async def get_lines(self, path: str, key: str = None) -> list[dict[str, Any]]:
        pass


class JsonFileService(FileService):
    SUPPORTED_EXTENSIONS = '.json'

    async def get_lines(self, path: str, key: str = None) -> list[dict[str, Any]]:
        async with aiofiles.open(path, 'r') as json_file:
            content = await json_file.read()
            data_from_file = json.loads(content)
        return data_from_file[key]


class TxtFileService(FileService):
    SUPPORTED_EXTENSIONS = '.txt'

    async def get_lines(self, path: str, key: str = None) -> list[dict[str, Any]]:
        cars_data = []

        async with aiofiles.open(path, 'r') as f:
            lines = [line.strip() if line.endswith('\n') else line for line in await f.readlines()]
            for line in lines:
                car_data = line.split(',')
                car = {
                    'model': car_data[0],
                    'price': int(car_data[1]),
                    'color': car_data[2],
                    'mileage': int(car_data[3]),
                    'components': car_data[4].split(':') if len(car_data[4]) > 0 else []
                }
                cars_data.append(car)
            return cars_data
