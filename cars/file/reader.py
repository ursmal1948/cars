import asyncio
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

    # Propagowanie wyjatkow.

    async def get_lines(self, path: str, key: str = None) -> list[dict[str, Any]]:
        async with aiofiles.open(path, 'r') as json_file:
            content = await json_file.read()
            data_from_file = json.loads(content)
        return data_from_file[key]


class TxtFileService(FileService):
    SUPPORTED_EXTENSIONS = '.txt'

    async def get_lines(self, path: str, key: str = None) -> list[dict[str, Any]]:
        cars_data = []
        attribute_data_type = [('model', str), ('price', int), ('color', str), ('mileage', int), ('components', list)]

        def parse(value: str, data_type: type) -> Any:
            if data_type == list:
                return value.split(':')
            return data_type(value)

        async with aiofiles.open(path, 'r') as f:
            lines = [line.strip() if line.endswith('\n') else line for line in await f.readlines()]
            for line in lines:
                car_data = line.split(',')
                car = [(attr, parse(value, data_type)) for (attr, data_type), value in
                       zip(attribute_data_type, car_data)]
                cars_data.append(dict(car))
            return cars_data
