import unittest
from cars.validator import CarsDataValidator


class TestCarsValidator(unittest.TestCase):

    def setUp(self):
        self.cars_validator = CarsDataValidator(r'^[A-Z\s]+$', ['SILVER', 'BLUE'])
        self.valid_car = {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500, 'components': ['BLUTEOOTH']}
        self.invalid_car = {'model': 'AUDI', 'price': -400, 'color': 'SILVER', 'mileage': 1200, 'components': ['ABS']}

    def test_validate_car_valid(self):
        validated_data = self.cars_validator.validate_item(self.valid_car)
        self.assertTrue(validated_data == {})

    def test_validate_car_invalid(self):
        validated_data = self.cars_validator.validate_item(self.invalid_car)
        self.assertFalse(validated_data == {})

    def test_validate_cars_when_all_valid(self):
        cars_data = [self.valid_car, self.valid_car]
        result = self.cars_validator.validate(cars_data)
        self.assertEqual(result,
                         [
                             {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500,
                              'components': ['BLUTEOOTH']},
                             {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500,
                              'components': ['BLUTEOOTH']}
                         ])

    def test_validate_cars_when_not_all_valid(self):
        cars_data = [self.valid_car, self.invalid_car]
        result = self.cars_validator.validate(cars_data)
        self.assertEqual(result,
                         [
                             {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500,
                              'components': ['BLUTEOOTH']}
                         ])

    def test_validate_cars_when_all_not_valid(self):
        cars_data = [self.invalid_car, self.invalid_car]
        result = self.cars_validator.validate(cars_data)
        self.assertEqual(result, [])
