from cars.model import Car
from cars.file.service import FromTxtFileToCar, FromJsonFileToCar, DataProcessor, DataFactoryType
from cars.file.reader import TxtFileService, JsonFileService
from cars.validator import CarsDataValidator
from cars.converter import AsyncCarsConverter
import unittest


class TestDataFactoryFromTxtFileToCar(unittest.TestCase):

    def setUp(self):
        self.factory = FromTxtFileToCar()

    def test_create_file_service(self):
        file_service = self.factory.create_file_service()
        self.assertIsInstance(file_service, TxtFileService)

    def test_create_validator(self):
        validator = self.factory.create_validator()
        self.assertIsInstance(validator, CarsDataValidator)
        self.assertEqual(validator.model_regex, r'^[A-Z\s]+$')
        self.assertEqual(validator.colors, ['SILVER', 'BLUE'])

    def test_create_converter(self):
        converter = self.factory.create_converter()
        self.assertIsInstance(converter, AsyncCarsConverter)


class TestDataFactoryFromJsonFileToCar(unittest.TestCase):

    def setUp(self):
        self.factory = FromJsonFileToCar()

    def test_create_file_service(self):
        file_service = self.factory.create_file_service()
        self.assertIsInstance(file_service, JsonFileService)

    def test_create_validator(self):
        validator = self.factory.create_validator()
        self.assertIsInstance(validator, CarsDataValidator)
        self.assertEqual(validator.model_regex, r'^[A-Z\s]+$')
        self.assertEqual(validator.colors, ['SILVER', 'BLUE'])

    def test_create_converter(self):
        converter = self.factory.create_converter()
        self.assertIsInstance(converter, AsyncCarsConverter)


class TestDataProcessorProcess:
    def test_text_data_processor(self, txt_path_correct_data):
        txt_data_factory = FromTxtFileToCar()
        processor = DataProcessor(txt_data_factory)
        cars = processor.process(txt_path_correct_data, None)
        assert cars == [
            Car(model='BMW', price=2000, color='BLUE', mileage=1500, components=['BLUETOOTH', 'ABS']),
            Car(model='OPEL', price=1000, color='SILVER', mileage=2000, components=['CAMERA', 'ABS'])
        ]

    def test_json_data_processor(self, json_path_correct_data):
        json_data_factory = FromJsonFileToCar()
        processor = DataProcessor(json_data_factory)
        cars = processor.process(json_path_correct_data, 'cars')

        assert cars == [
            Car(model='AUDI', price=9000, color='SILVER', mileage=1500, components=['CAMERA']),
            Car(model='TOYOTA', price=4000, color='BLUE', mileage=10000, components=['KEYLESS ENTRY', 'BLUETOOTH'])

        ]


class TestDataProcessorCreateProcessor(unittest.TestCase):

    def test_create_from_txt_factory(self):
        processor = DataProcessor.create_processor(DataFactoryType.FROM_TXT)
        self.assertIsInstance(processor.file_service, TxtFileService)
        self.assertIsInstance(processor.validator, CarsDataValidator)
        self.assertIsInstance(processor.converter, AsyncCarsConverter)

    def test_create_from_json_factory(self):
        processor = DataProcessor.create_processor(DataFactoryType.FROM_JSON)
        self.assertIsInstance(processor.file_service, JsonFileService)
        self.assertIsInstance(processor.validator, CarsDataValidator)
        self.assertIsInstance(processor.converter, AsyncCarsConverter)
