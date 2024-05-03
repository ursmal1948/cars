import pytest
from cars.model import Car


@pytest.fixture
def group_and_sort_service_cars_with_additional_cars(group_and_sort_service, toyota_car):
    group_and_sort_service.add_cars(toyota_car)
    return group_and_sort_service


class TestGroupAndSortServiceGetMostExpensiveCarForModel:
    def test_when_there_are_no_most_expensive_cars_for_model(self, group_and_sort_service):
        most_expensive_car = group_and_sort_service.get_most_expensive_car_for_model('OPEL')
        assert most_expensive_car == []

    def test_when_there_is_single_most_expensive_car_for_model(self, group_and_sort_service, toyota_car):
        most_expensive_car_for_model = group_and_sort_service.get_most_expensive_car_for_model('TOYOTA')
        assert most_expensive_car_for_model == toyota_car

    def test_when_there_are_multiple_most_expensive_cars_for_model(
            self,
            group_and_sort_service_cars_with_additional_cars, toyota_car
    ):
        most_expensive_cars_for_model = \
            group_and_sort_service_cars_with_additional_cars.get_most_expensive_car_for_model(
                'TOYOTA'
            )
        assert most_expensive_cars_for_model == [toyota_car, toyota_car]
