from cars.model import Car
import pytest


class TestFilterServiceGetCarsWithHigherMileageThan:

    def test_when_mileage_is_negative_value(self, filter_service):
        with pytest.raises(ValueError) as e:
            filter_service.get_cars_with_higher_mileage_than(-300)
        assert str(e.value).startswith("Mileage limit must be a non-negative value")

    def test_when_there_is_empty_expected_cars_collection(self, filter_service):
        result = filter_service.get_cars_with_higher_mileage_than(2000)
        assert result == []

    def test_when_there_are_not_all_cars_with_expected_mileage(self, filter_service, bmw_car, audi_car):
        result = filter_service.get_cars_with_higher_mileage_than(999)
        assert result == [bmw_car, audi_car]

    def test_when_there_are_all_cars_with_expected_mileage(self, filter_service, bmw_car, audi_car, toyota_car):
        result = filter_service.get_cars_with_higher_mileage_than(99)
        assert result == [bmw_car, audi_car, toyota_car]
