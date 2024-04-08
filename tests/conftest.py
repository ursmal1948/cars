import pytest


@pytest.fixture
def txt_path_correct_data():
    return 'test_data/cars_test.txt'


@pytest.fixture
def json_path_correct_data():
    return 'test_data/cars_test.json'
