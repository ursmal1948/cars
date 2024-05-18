import unittest

import pytest

from cars.validator import CarsDataValidator


class TestCarsValidator:
    @pytest.fixture
    def valid_data_car(self):
        return {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500, 'components': ['BLUTEOOTH']}

    @pytest.fixture
    def invalid_data_car(self):
        return {'model': 'AUDI', 'price': -400, 'color': 'SILVER', 'mileage': 1200, 'components': ['ABS']}

    @pytest.fixture
    def cars_validator(self):
        return CarsDataValidator(r'^[A-Z\s]+$', ['SILVER', 'BLUE'])

    @pytest.mark.asyncio
    async def test_validate_car_valid(self, valid_data_car, cars_validator):
        validated_data = await cars_validator.validate_item(valid_data_car)
        assert validated_data == {}

    @pytest.mark.asyncio
    async def test_validate_car_invalid(self, invalid_data_car, cars_validator):
        validated_data = await cars_validator.validate_item(invalid_data_car)
        assert not validated_data == {}

    @pytest.mark.asyncio
    async def test_validate_cars_when_all_valid(self, valid_data_car, cars_validator):
        cars_data = [valid_data_car, valid_data_car]
        result = await cars_validator.validate(cars_data)
        assert result == [
            {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500,
             'components': ['BLUTEOOTH']},
            {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500,
             'components': ['BLUTEOOTH']}
        ]

    @pytest.mark.asyncio
    async def test_validate_cars_when_not_all_valid(self, valid_data_car, invalid_data_car, cars_validator):
        cars_data = [valid_data_car, invalid_data_car]
        result = await cars_validator.validate(cars_data)
        assert result == [
            {'model': 'BMW', 'price': 300, 'color': 'BLUE', 'mileage': 500,
             'components': ['BLUTEOOTH']}
        ]

    @pytest.mark.asyncio
    async def test_validate_cars_when_all_invalid(self, invalid_data_car, cars_validator):
        cars_data = [invalid_data_car, invalid_data_car]
        result = await cars_validator.validate(cars_data)
        assert result == []
