import unittest
from cars.validator import CarsValidator


class TestCarsData:
    VALID_CAR_1 = {'model': 'AUDI', 'price': 900, 'color': 'SILVER', 'mileage': 1200, 'components': ['ABS']}
    VALID_CAR_2 = {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500, 'components': ['BLUTEOOTH']}
    INVALID_CAR_1 = {'model': 'AUDI', 'price': -400, 'color': 'SILVER', 'mileage': 1200, 'components': ['ABS']}
    INVALID_CAR_2 = {'model': 'RANGE ROVER', 'price': 3000, 'color': 'BLACK', 'mileage': -100,
                     'components': ['EVASIVE STEERING']}


class TestCarsValidator(unittest.TestCase):

    def setUp(self):
        self.cars_validator = CarsValidator(r'^[A-Z\s]+$', ['SILVER', 'BLUE'])

    def test_validate_car_valid(self):
        validated_data = self.cars_validator.validate_item(TestCarsData.VALID_CAR_1)
        self.assertTrue(validated_data == {})

    def test_validate_car_invalid(self):
        validated_data = self.cars_validator.validate_item(TestCarsData.INVALID_CAR_1)
        self.assertFalse(validated_data == {})

    def test_validate_cars_when_all_valid(self):
        cars_data = [TestCarsData.VALID_CAR_1, TestCarsData.VALID_CAR_2]
        result = self.cars_validator.validate(cars_data)
        self.assertEqual(result,
                         [{'model': 'AUDI', 'price': 900, 'color': 'SILVER', 'mileage': 1200, 'components': ['ABS']},
                          {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500, 'components': ['BLUTEOOTH']}]
                         )

    def test_validate_cars_when_not_all_valid(self):
        cars_data = [TestCarsData.VALID_CAR_1, TestCarsData.INVALID_CAR_1, TestCarsData.INVALID_CAR_2]
        result = self.cars_validator.validate(cars_data)
        self.assertEqual(result,
                         [{'model': 'AUDI', 'price': 900, 'color': 'SILVER', 'mileage': 1200, 'components': ['ABS']}])

    def test_validate_cars_when_all_not_valid(self):
        cars_data = [TestCarsData.INVALID_CAR_1, TestCarsData.INVALID_CAR_2]
        result = self.cars_validator.validate(cars_data)
        self.assertEqual(result, [])
