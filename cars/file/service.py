import json
from dataclasses import dataclass, field
from typing import Any


class JsonFileService:
    SUPPORTED_EXTENSIONS = '.json'

    @staticmethod
    def get_lines(path: str, key: str) -> list[dict[str, Any]]:
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

#
# d = JsonFileService.get_lines('../../test_data/cars_test.json', 'cars')
# print(list(d[0].values()))
# print(list(d[1].values()))
