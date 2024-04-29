import pytest
from cars.model import Car


@pytest.fixture
def filter_service_cars_with_additional_cars(filter_service_cars):
    filter_service_cars.add_cars([Car('MAZDA', 300, 'SILVER', 200, []), Car('OPEL', 50, 'WHITE', 2000, [])])
    return filter_service_cars


class TestFilterServiceGetExtremePricedCars:
    def test_when_there_is_more_than_one(self, filter_service_cars_with_additional_cars):
        most_priced_cars = filter_service_cars_with_additional_cars.get_extreme_priced_cars(lambda cars: max(cars))
        assert most_priced_cars == [Car('AUDI', 300, 'BLUE', 1000, []),
                                    Car('MAZDA', 300, 'SILVER', 200, [])]

        least_prices_cars = filter_service_cars_with_additional_cars.get_extreme_priced_cars(lambda cars: min(cars))
        assert least_prices_cars == [Car('TOYOTA', 50, 'SILVER', 200, []),
                                     Car('OPEL', 50, 'WHITE', 2000, [])]

    def test_when_there_is_one(self, filter_service_cars):
        assert filter_service_cars.get_extreme_priced_cars(lambda cars: max(cars)) == Car('AUDI', 300, 'BLUE', 1000, [])
        assert filter_service_cars.get_extreme_priced_cars(lambda cars: min(cars)) == Car('TOYOTA', 50, 'SILVER', 200,
                                                                                          [])
