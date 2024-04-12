import pytest
from cars.model import Car

from cars.cars_service.group_and_sort import GroupAndSortService


@pytest.fixture
def test_cars_service():
    return GroupAndSortService([
        Car('AUDI', 1, 'WHITE', 10),
        Car('BMW', 2, 'SILVER', 20),
        Car('FORD', 3, 'RED', 30),
        Car('FORD', 3, 'YELLOW', 40)
    ])


class TestGroupAndSortServiceGetMostExpensiveCarForModel:
    def test_when_there_are_no_most_expensive_cars_for_model(self, test_cars_service):
        most_expensive_car = test_cars_service.get_most_expensive_car_for_model('OPEL')
        assert most_expensive_car == []

    def test_when_there_is_single_most_expensive_car_for_model(self, test_cars_service):
        most_expensive_car_for_model = test_cars_service.get_most_expensive_car_for_model('BMW')
        assert most_expensive_car_for_model == Car('BMW', 2, 'SILVER', 20)

    def test_when_there_are_multiple_most_expensive_cars_for_model(self, test_cars_service):
        most_expensive_cars_for_model = test_cars_service.get_most_expensive_car_for_model('FORD')
        assert most_expensive_cars_for_model == [Car('FORD', 3, 'RED', 30),
                                                 Car('FORD', 3, 'YELLOW', 40)]
