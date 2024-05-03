import pytest
from cars.model import Car


@pytest.fixture
def mazda_car():
    return Car('MAZDA', 300, 'SILVER', 200, [])


@pytest.fixture
def opel_car():
    return Car('OPEL', 50, 'WHITE', 2000, [])


@pytest.fixture
def service_with_additional_cars(filter_service, mazda_car, opel_car):
    filter_service.add_cars([mazda_car, opel_car])
    return filter_service


class TestFilterServiceGetExtremePricedCars:
    def test_when_there_is_more_than_one(self, service_with_additional_cars, audi_car, mazda_car,
                                         toyota_car, opel_car):
        most_priced_cars = service_with_additional_cars.get_extreme_priced_cars(lambda cars: max(cars))
        assert most_priced_cars == [audi_car, mazda_car]

        least_prices_cars = service_with_additional_cars.get_extreme_priced_cars(lambda cars: min(cars))
        assert least_prices_cars == [toyota_car, opel_car]

    def test_when_there_is_one(self, filter_service, audi_car, toyota_car):
        assert filter_service.get_extreme_priced_cars(lambda cars: max(cars)) == audi_car
        assert filter_service.get_extreme_priced_cars(lambda cars: min(cars)) == toyota_car
