import pytest
from cars.model import Car


@pytest.fixture
def group_and_sort_service_cars_with_same_price_and_model_car(group_and_sort_service_cars):
    group_and_sort_service_cars.add_cars(Car('TOYOTA', 3, 'SILVER', 500, []))
    return group_and_sort_service_cars


class TestGroupAndSortServiceGetMostExpensiveCarForModel:
    def test_when_there_are_no_most_expensive_cars_for_model(self, group_and_sort_service_cars):
        most_expensive_car = group_and_sort_service_cars.get_most_expensive_car_for_model('OPEL')
        assert most_expensive_car == []

    def test_when_there_is_single_most_expensive_car_for_model(self, group_and_sort_service_cars):
        most_expensive_car_for_model = group_and_sort_service_cars.get_most_expensive_car_for_model('TOYOTA')
        assert most_expensive_car_for_model == Car('TOYOTA', 3, 'SILVER', 200)

    def test_when_there_are_multiple_most_expensive_cars_for_model(
            self,
            group_and_sort_service_cars_with_same_price_and_model_car
    ):
        most_expensive_cars_for_model = \
            group_and_sort_service_cars_with_same_price_and_model_car.get_most_expensive_car_for_model(
                'TOYOTA'
            )
        assert most_expensive_cars_for_model == [Car('TOYOTA', 3, 'SILVER', 200, []),
                                                 (Car('TOYOTA', 3, 'SILVER', 500, []))]
