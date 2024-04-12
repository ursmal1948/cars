import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any
from enum import Enum
import re
from cars.model import Car
from typing import Self


class FileService(ABC):

    @abstractmethod
    def get_lines(self, path: str, key: str = None):
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
        with open(path, 'r') as f:
            lines = [line.strip() if line.endswith('\n') else line for line in f.readlines()]
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


class Validator(ABC):
    @abstractmethod
    def validate(self, data: dict[str, Any]) -> list[dict[str, Any]]:
        pass


@dataclass
class CarsValidator(Validator):
    model_regex: str
    colors: list[str]

    def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        validated_cars_data = []
        for car_data in data:
            errors = {}

            if 'model' not in car_data:
                errors |= {'model': ['not found']}
            elif not re.match(self.model_regex, car_data['model']):
                errors |= {'model': ['does not match the regex']}
            if 'price' not in car_data:
                errors |= {'price': ['not found']}
            elif not car_data['price'] >= 0:
                errors |= {'price': ['incorrect value']}
            if 'color' not in car_data:
                errors |= {'color': ['not found']}
            elif car_data['color'] not in self.colors:
                errors |= {'color': ['incorrect color of the car']}
            if 'mileage' not in car_data:
                errors |= {'mileage': ['not found']}
            elif not car_data['mileage'] >= 0:
                errors |= {'mileage': ['incorrect value']}
            if 'components' not in car_data:
                errors |= {'components': ['not found']}
            else:
                for c in car_data['components']:
                    if not re.match(self.model_regex, c):
                        errors.update({'components': ['does not match the regex']})
            if len(errors) == 0:
                validated_cars_data.append(car_data)
        return validated_cars_data


class Converter(ABC):
    @abstractmethod
    def convert(self, data: list[dict[str, Any]]) -> Car:
        pass


class CarsConverter(Converter):
    def convert(self, data: list[dict[str, Any]]) -> list[Car]:
        return [Car.from_dict(car) for car in data]


class DataFactory(ABC):
    @abstractmethod
    def create_file_service(self) -> FileService:
        pass

    @abstractmethod
    def create_validator(self) -> Validator:
        pass

    @abstractmethod
    def create_converter(self) -> Converter:
        pass


class DataFactoryType(Enum):
    FROM_TXT = 0,
    FROM_JSON = 1


@dataclass
class FromTxtFileToCar(DataFactory):

    def create_file_service(self) -> FileService:
        return TxtFileService()

    def create_validator(self) -> 'Validator':
        return CarsValidator(r'^[A-Z\s]+$', ['BLUE', 'SILVER'])

    def create_converter(self) -> Converter:
        return CarsConverter()


class FromJsonFileToCar(DataFactory):

    def create_file_service(self) -> FileService:
        return JsonFileService()

    def create_validator(self) -> 'Validator':
        return CarsValidator(r'^[A-Z\s]+$', ['BLUE', 'SILVER'])

    def create_converter(self) -> Converter:
        return CarsConverter()


class DataProcessor:
    def __init__(self, data_factory: DataFactory):
        self.file_service = data_factory.create_file_service()
        self.validator = data_factory.create_validator()
        self.converter = data_factory.create_converter()

    def process(self, path: str, key: str = None):
        data_from_resource = self.file_service.get_lines(path, key)
        validated_data = self.validator.validate(data_from_resource)
        return self.converter.convert(validated_data)

    @classmethod
    def create_processor(cls, factory_type: DataFactoryType) -> Self:
        match factory_type:
            case factory_type.FROM_TXT:
                return cls(FromTxtFileToCar())
            case factory_type.FROM_JSON:
                return cls(FromJsonFileToCar())

#
# json_data_factory = FromJsonFileToCar()
# processor = DataProcessor(json_data_factory)
# cars1 = processor.process('../../data/cars.json', 'cars')
#
# txt_data_factory = FromTxtFileToCar()
# processor2 = DataProcessor(txt_data_factory)
# cars2 = processor2.process('../../data/cars.txt', None)
#
# print(cars1)
# print(cars2)
