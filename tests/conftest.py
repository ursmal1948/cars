import pytest
from cars.model import Car


@pytest.fixture
def txt_path_correct_data():
    return 'test_data/cars_test.txt'


@pytest.fixture
def json_path_correct_data():
    return 'test_data/cars_test.json'


@pytest.fixture
def test_car_example():
    return Car('HONDA', 200, 'BLUE', 200, ['ABS', 'AIR CONDITIONING'])
