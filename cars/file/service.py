from abc import ABC, abstractmethod
from enum import Enum
from cars.file.reader import FileService, JsonFileService, TxtFileService
from cars.converter import Converter, CarsConverter
from cars.validator import Validator, CarsDataValidator


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


class FromTxtFileToCar(DataFactory):

    def create_file_service(self) -> FileService:
        return TxtFileService()

    def create_validator(self) -> Validator:
        return CarsDataValidator(r'^[A-Z\s]+$', ['SILVER', 'BLUE'])

    def create_converter(self) -> Converter:
        return CarsConverter()


class FromJsonFileToCar(DataFactory):

    def create_file_service(self) -> FileService:
        return JsonFileService()

    def create_validator(self) -> 'Validator':
        return CarsDataValidator(r'^[A-Z\s]+$', ['SILVER', 'BLUE'])

    def create_converter(self) -> Converter:
        return CarsConverter()


class DataProcessor:
    def __init__(self, data_factory: DataFactory):
        self.file_service = data_factory.create_file_service()
        self.validator = data_factory.create_validator()
        self.converter = data_factory.create_converter()

    async def process(self, path: str, key: str = None):
        data_from_resource = await self.file_service.get_lines(path, key)
        validated_data = await self.validator.validate(data_from_resource)
        return await self.converter.convert(validated_data)

    @classmethod
    async def create_processor(cls, factory_type: DataFactoryType) -> 'DataProcessor':
        match factory_type:
            case factory_type.FROM_TXT:
                return cls(FromTxtFileToCar())
            case factory_type.FROM_JSON:
                return cls(FromJsonFileToCar())
