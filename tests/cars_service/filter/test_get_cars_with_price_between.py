import pytest


class TestFilterServiceGetCarsWithPriceBetween:

    def test_when_price_range_is_not_correct(self, filter_service):
        with pytest.raises(ValueError) as e:
            filter_service.get_cars_with_price_between(20, 10)
        assert str(e.value).startswith('Price range is not correct')

    def test_when_there_is_empty_cars_collection(self, filter_service):
        cars = filter_service.get_cars_with_price_between(10, 20)
        assert cars == []

    def test_when_there_are_not_all_cars_within_price_range(self, filter_service, bmw_car, toyota_car):
        cars = filter_service.get_cars_with_price_between(50, 100)
        assert cars == [
            bmw_car, toyota_car
        ]

    def test_when_there_are_all_cars_within_price_range(self, filter_service, audi_car, bmw_car, toyota_car):
        cars = filter_service.get_cars_with_price_between(50, 300)
        assert cars == [audi_car, bmw_car, toyota_car]
