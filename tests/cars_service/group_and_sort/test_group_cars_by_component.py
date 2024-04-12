from cars.cars_service.group_and_sort import GroupAndSortService
from cars.model import Car
import pytest


@pytest.fixture
def test_cars_service():
    return GroupAndSortService([
        Car('AUDI', 1, 'WHITE', 10, ['ABS', 'AIR CONDITIONING']),
        Car('BMW', 2, 'SILVER', 20, ['ABS']),
        Car('FORD', 3, 'RED', 30, ['BLUETOOTH']),
        Car('FORD', 3, 'YELLOW', 40, ['AIR CONDITIONING']),
    ])


class TestGroupAndSortServiceGroupByComponent:

    def test_when_component_is_in_one_car(self, test_cars_service):
        result = test_cars_service.group_cars_by_component()['BLUETOOTH'][0]
        assert result == Car('FORD', 3, 'RED', 30, ['BLUETOOTH'])

    def test_when_multiple_cars_have_same_component(self, test_cars_service):
        result = test_cars_service.group_cars_by_component()['ABS']
        assert result == [
            Car('AUDI', 1, 'WHITE', 10, ['ABS', 'AIR CONDITIONING']),
            Car('BMW', 2, 'SILVER', 20, ['ABS'])
        ]

        result2 = test_cars_service.group_cars_by_component()['AIR CONDITIONING']
        assert result2 == [
            Car('AUDI', 1, 'WHITE', 10, ['ABS', 'AIR CONDITIONING']),
            Car('FORD', 3, 'YELLOW', 40, ['AIR CONDITIONING'])
        ]
