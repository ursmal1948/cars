import unittest
from cars.file.reader import JsonFileService
from cars.file.service import FromJsonFileToCar
from cars.validator import CarsValidator
from cars.converter import CarsConverter


class DataFactoryFromTxtFileToCar(unittest.TestCase):

    def setUp(self):
        self.factory = FromJsonFileToCar()

    def test_create_file_service(self):
        file_service = self.factory.create_file_service()
        self.assertIsInstance(file_service, JsonFileService)

    def test_create_validator(self):
        validator = self.factory.create_validator()
        self.assertIsInstance(validator, CarsValidator)
        self.assertEqual(validator.model_regex, r'^[A-Z\s]+$')
        self.assertEqual(validator.colors, ['SILVER', 'BLUE'])

    def test_create_converter(self):
        converter = self.factory.create_converter()
        self.assertIsInstance(converter, CarsConverter)

