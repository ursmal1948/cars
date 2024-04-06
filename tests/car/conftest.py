from cars.model import Car
import pytest


@pytest.fixture
def test_car_example():
    return Car('HONDA', 200, 'BLUE', 200, ['ABS', 'AIR CONDITIONING'])
