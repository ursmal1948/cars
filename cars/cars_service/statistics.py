from dataclasses import dataclass, field
from decimal import Decimal
from cars.enums import Category
from cars.model import Car


@dataclass
class Statistics:
    min_v: Decimal
    avg_v: Decimal
    max_v: Decimal

    """
    Represents statistical information about a category of cars.

    Attributes:
        min_v (Decimal): The minimum value of the specified category among the cars.
        avg_v (Decimal): The average value of the specified category among the cars.
        max_v (Decimal): The maximum value of the specified category among the cars.
    """


@dataclass
class StatisticsService:
    cars: list[Car] = field(default_factory=list[Car])

    def get_statistics_for(self, category: Category) -> Statistics:
        """
        Calculate statistics for the specified category of cars (price or mileage).

        Parameters:
            category (Category): The category for which statistics will be calculated.

        Returns:
            Statistics: A Statistics object containing the minimum, average, and maximum values
                        of the specified category among the cars.

        Raises:
            AttributeError: If the category is invalid or not applicable to any cars.
        """

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
