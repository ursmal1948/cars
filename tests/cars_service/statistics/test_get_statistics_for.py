import pytest
from cars.cars_service.statistics import StatisticsService, Statistics
from cars.enums import Category
from cars.model import Car
from decimal import Decimal


@pytest.fixture
def statistics_test_service():
    return StatisticsService([
        Car("TOYOTA", 1000, "WHITE", 300, []),
        Car("FORD", 5000, "WHITE", 100, []),
        Car("FORD", 9000, "WHITE", 800, []),
    ])


class TestStatisticsServiceGetStatisticsFor:

    def test_for_mileage(self, statistics_test_service):
        mileage_statistics = statistics_test_service.get_statistics_for(Category.MILEAGE)
        assert mileage_statistics == Statistics(
            Decimal("100"),
            Decimal("400"),
            Decimal("800")
        )

    def test_for_price(self, statistics_test_service):
        price_statistics = statistics_test_service.get_statistics_for(Category.PRICE)
        assert price_statistics == Statistics(
            Decimal("1000"),
            Decimal("5000"),
            Decimal("9000"),
        )

    def test_when_wrong_attribute(self, statistics_test_service):
        with pytest.raises(AttributeError) as e:
            statistics_test_service.get_statistics_for(Category.INVALID_CATEGORY)
        assert str(e.value).startswith("Invalid category")
