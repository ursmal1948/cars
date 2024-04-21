import unittest
from cars.validator import CarsValidator


class TestCarsValidatorMethods(unittest.TestCase):
    def setUp(self):
        self.cars_validator = CarsValidator(r'^[A-Z\s]+$', ['SILVER', 'BLUE'])

    def test_validate_model(self):
        self.assertTrue(self.cars_validator._validate_model('RANGE ROVER'))
        self.assertFalse(self.cars_validator._validate_model('car'))

    def test_validate_price(self):
        self.assertTrue(self.cars_validator._validate_price(300))
        self.assertFalse(self.cars_validator._validate_price(-300))

    def test_validate_color(self):
        self.assertTrue(self.cars_validator._validate_color('SILVER'))
        self.assertFalse(self.cars_validator._validate_color('RED'))

    def test_validate_mileage(self):
        self.assertTrue(self.cars_validator._validate_mileage(4000))
        self.assertFalse(self.cars_validator._validate_mileage(-4000))

    def test_validate_components(self):
        self.assertTrue(self.cars_validator._validate_components(['ABS', 'BLUETOOTH']))
        self.assertFalse(self.cars_validator._validate_components(['some component']))
