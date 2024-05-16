import pytest

from cars.converter import AsyncCarsConverter
from cars.model import Car


class TestConverter:

    @pytest.fixture
    def test_cars(self):
        return [
            {'model': 'AUDI', 'price': 900, 'color': 'SILVER', 'mileage': 1200, 'components': ['ABS', 'BLUETOOTH']},
            {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500,
             'components': ['AIR CONDITIONING', 'CAMERA']},
            {'model': 'OPEL', 'price': 5000, 'color': 'WHITE', 'mileage': 700,
             'components': ['EVASIVE STEERING']}]

    def test_car_converter(self, test_cars):
        cars_converter = AsyncCarsConverter().convert(test_cars)
        assert cars_converter == [
            Car('AUDI', 900, 'SILVER', 1200, ['ABS', 'BLUETOOTH']),
            Car('BMW', 300, 'BLUE', 500, ['AIR CONDITIONING', 'CAMERA']),
            Car('OPEL', 5000, 'WHITE', 700, ['EVASIVE STEERING'])
        ]
