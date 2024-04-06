import pytest
from cars.model import Car


class TestCarHasComponent:

    def test_when_car_has_expected_component(self, test_car_example):
        assert test_car_example.has_component('ABS')

    def test_when_car_has_not_expected_component(self, test_car_example):
        assert not test_car_example.has_component('BLUETOOTH')
