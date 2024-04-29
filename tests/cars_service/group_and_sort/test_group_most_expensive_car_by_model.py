from cars.model import Car
import pytest


@pytest.fixture
def group_and_sort_service_cars_with_additional_cars(group_and_sort_service_cars):
    group_and_sort_service_cars.add_cars([Car('AUDI', 2, 'WHITE', 100, []), Car('BMW', 1, 'BLACK', 2000, [])])
    return group_and_sort_service_cars


class TestGroupAndSortServiceGroupMostExpensiveCarsByModel:

    def test_when_models_have_one_most_expensive_car(self, group_and_sort_service_cars):
        result = group_and_sort_service_cars.group_most_expensive_cars_by_model()
        assert result == {'BMW': Car('BMW', 1, 'WHITE', 2000, []),
                          'AUDI': Car('AUDI', 2, 'BLUE', 1000, []),
                          'TOYOTA': Car('TOYOTA', 3, 'SILVER', 200, [])}

    def test_when_models_have_more_than_one_most_expensive_car(self, group_and_sort_service_cars_with_additional_cars):
        result = group_and_sort_service_cars_with_additional_cars.group_most_expensive_cars_by_model()
        assert result == {'AUDI': [Car('AUDI', 2, 'BLUE', 1000, []),
                                   Car('AUDI', 2, 'WHITE', 100, [])],
                          'BMW': [Car('BMW', 1, 'WHITE', 2000, []), Car('BMW', 1, 'BLACK', 2000, [])],
                          'TOYOTA': Car('TOYOTA', 3, 'SILVER', 200, [])}
