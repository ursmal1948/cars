import pytest
from cars.cars_service.group_and_sort import GroupAndSortService
from cars.cars_service.filter import FilterService
from cars.model import Car


@pytest.fixture
def bmw_car():
    return Car('BMW', 100, 'WHITE', 2000, ['ABS'])


@pytest.fixture
def audi_car():
    return Car('AUDI', 300, 'BLUE', 1000, ['ABS', 'AIR CONDITIONING'])


@pytest.fixture
def toyota_car():
    return Car('TOYOTA', 50, 'SILVER', 200, ['BLUETOOTH'])


@pytest.fixture
def group_and_sort_service(bmw_car, audi_car, toyota_car):
    return GroupAndSortService(
        [
            bmw_car,
            audi_car,
            toyota_car
        ]
    )


@pytest.fixture
def filter_service(bmw_car, audi_car, toyota_car):
    return FilterService(
        [
            bmw_car,
            audi_car,
            toyota_car
        ]
    )
