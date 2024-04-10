from dataclasses import dataclass, field
from decimal import Decimal
from cars.model import Car
from cars.enums import Category
from cars.cars_service.service import CarsService


@dataclass
class Statistics:
    min_v: Decimal
    avg_v: Decimal
    max_v: Decimal


@dataclass
class StatisticsService(CarsService):

    def get_statistics_for(self, category: Category) -> Statistics:
        attribute_name = category.name.lower()
        if not all(hasattr(car, attribute_name) for car in self.cars):
            raise AttributeError(f'Invalid category: {category}')

        values = [getattr(car, attribute_name) for car in self.cars]
        avg_value = Decimal(sum(values) / len(values))
        return Statistics(
            min_v=Decimal(min(values)),
            avg_v=avg_value,
            max_v=Decimal(max(values))
        )
