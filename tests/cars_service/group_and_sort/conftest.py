import pytest
from cars.cars_service.group_and_sort import GroupAndSortService
from cars.model import Car


@pytest.fixture
def group_and_sort_service_cars():
    return GroupAndSortService(
        [
            Car('BMW', 1, 'WHITE', 2000, []),
            Car('AUDI', 2, 'BLUE', 1000, []),
            Car('TOYOTA', 3, 'SILVER', 200, [])
        ]
    )
