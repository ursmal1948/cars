from cars.converter import CarsConverter
from cars.model import Car


class TestDataCars:
    CAR_1 = {'model': 'AUDI', 'price': 900, 'color': 'SILVER', 'mileage': 1200, 'components': ['ABS', 'BLUETOOTH']}
    CAR_2 = {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500,
             'components': ['AIR CONDITIONING', 'CAMERA']}
    CAR_3 = {'model': 'OPEL', 'price': 5000, 'color': 'WHITE', 'mileage': 700,
             'components': ['EVASIVE STEERING']}


class TestConverter:
    def test_car_converter(self):
        test_cars = [TestDataCars.CAR_1, TestDataCars.CAR_2, TestDataCars.CAR_3]
        cars_converter = CarsConverter().convert(test_cars)
        assert cars_converter == [
            Car('AUDI', 900,'SILVER', 1200, ['ABS', 'BLUETOOTH']),
            Car('BMW', 300, 'BLUE', 500, ['AIR CONDITIONING', 'CAMERA']),
            Car('OPEL', 5000, 'WHITE', 700, ['EVASIVE STEERING'])
        ]
