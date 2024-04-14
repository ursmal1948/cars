import unittest
from cars.file.reader import TxtFileService
from cars.file.service import FromTxtFileToCar
from cars.validator import CarsValidator
from cars.converter import CarsConverter


class DataFactoryFromTxtFileToCar(unittest.TestCase):

    def setUp(self):
        self.factory = FromTxtFileToCar()

    def test_create_file_service(self):
        file_service = self.factory.create_file_service()
        self.assertIsInstance(file_service, TxtFileService)

    def test_create_validator(self):
        validator = self.factory.create_validator()
        self.assertIsInstance(validator, CarsValidator)
        self.assertEqual(validator.model_regex, r'^[A-Z\s]+$')
        self.assertEqual(validator.colors, ['SILVER', 'BLUE'])

    def test_create_converter(self):
        converter = self.factory.create_converter()
        self.assertIsInstance(converter, CarsConverter)
