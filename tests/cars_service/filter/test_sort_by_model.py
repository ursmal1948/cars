from cars.model import Car
from cars.cars_service.filter import FilterService


class TestFilterServiceSortByModel:
    car_1 = Car('HONDA', 10, 'SILVER', 20, [])
    car_2 = Car('AUDI', 20, 'WHITE', 30, [])
    car_3 = Car('HONDA', 30, 'BLACK', 40, [])

    def test_when_car_1_greater_than_car_2(self):
        assert FilterService.sort_by_model(self.car_1, self.car_2) > 0

    def test_when_equal(self):
        assert FilterService.sort_by_model(self.car_1, self.car_3) == 0
