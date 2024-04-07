from dataclasses import dataclass, field
from decimal import Decimal
from cars.model import Car
from cars.enums import Category


@dataclass
class Statistics:
    min_v: Decimal
    avg_v: Decimal
    max_v: Decimal


@dataclass
class StatisticsService:
    cars: list[Car] = field(default_factory=list)

    def get_statistics_for_mileage(self) -> Statistics:
        mileage_values = [car.mileage for car in self.cars]
        avg_value = Decimal(sum(mileage_values) / len(mileage_values))
        return Statistics(
            min_v=Decimal(min(mileage_values)),
            avg_v=avg_value,
            max_v=Decimal(max(mileage_values))
        )

    def get_statistics_for_price(self) -> Statistics:
        price_values = [car.price for car in self.cars]
        avg_value = Decimal(sum(price_values) / len(price_values))
        return Statistics(
            min_v=Decimal(min(price_values)),
            avg_v=avg_value,
            max_v=Decimal(max(price_values))
        )

    def get_statistics_for(self, category: Category) -> Statistics:
        match category:
            case category.PRICE:
                return self.get_statistics_for_price()
            case category.MILEAGE:
                return self.get_statistics_for_mileage()
            case _:
                raise AttributeError('Incorrect category')
