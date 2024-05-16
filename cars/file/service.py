from abc import ABC, abstractmethod
from enum import Enum
from cars.file.reader import FileService, JsonFileService, TxtFileService
from cars.converter import AsyncConverter, AsyncCarsConverter
from cars.validator import AsyncValidator, CarsDataValidator
from typing import Awaitable


class DataFactory(ABC):
    @abstractmethod
    async def create_file_service(self) -> Awaitable[FileService]:
        pass

    @abstractmethod
    async def create_validator(self) -> Awaitable[AsyncValidator]:
        pass

    @abstractmethod
    async def create_converter(self) -> Awaitable[AsyncConverter]:
        pass


class DataFactoryType(Enum):
    FROM_TXT = 0,
    FROM_JSON = 1


class FromTxtFileToCar(DataFactory):

    async def create_file_service(self) -> FileService:
        return TxtFileService()

    async def create_validator(self) -> AsyncValidator:
        return CarsDataValidator(r'^[A-Z\s]+$', ['SILVER', 'BLUE'])

    async def create_converter(self) -> AsyncConverter:
        return AsyncCarsConverter()


class FromJsonFileToCar(DataFactory):

    async def create_file_service(self) -> FileService:
        return JsonFileService()

    async def create_validator(self) -> 'AsyncValidator':
        return CarsDataValidator(r'^[A-Z\s]+$', ['SILVER', 'BLUE'])

    async def create_converter(self) -> AsyncConverter:
        return AsyncCarsConverter()


class DataProcessor:
    def __init__(self, data_factory: DataFactory):
        self.file_service = None
        self.validator = None
        self.converter = None
        self.data_factory = data_factory

    async def initialize(self):
        self.file_service = await self.data_factory.create_file_service()
        self.validator = await self.data_factory.create_validator()
        self.converter = await self.data_factory.create_converter()

    async def process(self, path: str, key: str = None):
        if self.file_service is None or self.validator is None or self.converter is None:
            await self.initialize()
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
