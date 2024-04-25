import pytest
from cars.model import Car


class TestFilterServiceGetCarsWithPriceBetween:

    def test_when_price_range_is_not_correct(self, filter_service_cars):
        with pytest.raises(ValueError) as e:
            filter_service_cars.get_cars_with_price_between(20, 10)
        assert str(e.value).startswith('Price range is not correct')

    def test_when_there_is_empty_cars_collection(self, filter_service_cars):
        cars = filter_service_cars.get_cars_with_price_between(10, 20)
        assert cars == []

    def test_when_there_are_not_all_cars_within_price_range(self, filter_service_cars):
        cars = filter_service_cars.get_cars_with_price_between(50, 100)
        assert cars == [
            Car('BMW', 100, 'WHITE', 2000, []),
            Car('TOYOTA', 50, 'SILVER', 200, [])
        ]

    def test_when_there_are_all_cars_within_price_range(self, filter_service_cars):
        cars = filter_service_cars.get_cars_with_price_between(50, 300)
        assert cars == [Car('AUDI', 300, 'BLUE', 1000, []),
                        Car('BMW', 100, 'WHITE', 2000, []),
                        Car('TOYOTA', 50, 'SILVER', 200, [])]
