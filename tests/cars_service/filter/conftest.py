import pytest
from cars.cars_service.filter import FilterService
from cars.model import Car


@pytest.fixture
def filter_service_cars():
    return FilterService(
        [
            Car('BMW', 100, 'WHITE', 2000, []),
            Car('AUDI', 300, 'BLUE', 1000, []),
            Car('TOYOTA', 50, 'SILVER', 200, [])
        ]
    )
