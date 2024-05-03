import logging

import pytest


@pytest.fixture
def group_and_sort_service_cars_with_additional_cars(group_and_sort_service, audi_car, bmw_car):
    group_and_sort_service.add_cars([audi_car, bmw_car])
    return group_and_sort_service


class TestGroupAndSortServiceGroupMostExpensiveCarsByModel:

    def test_when_models_have_one_most_expensive_car(self, group_and_sort_service, bmw_car, audi_car, toyota_car):
        result = group_and_sort_service.group_most_expensive_cars_by_model()
        assert result == {'BMW': bmw_car, 'AUDI': audi_car, 'TOYOTA': toyota_car}

    def test_when_models_have_more_than_one_most_expensive_car(
            self,
            group_and_sort_service_cars_with_additional_cars,
            bmw_car,
            audi_car,
            toyota_car
    ):
        result = group_and_sort_service_cars_with_additional_cars.group_most_expensive_cars_by_model()
        assert result == {'AUDI': [audi_car, audi_car],
                          'BMW': [bmw_car, bmw_car],
                          'TOYOTA': toyota_car}
