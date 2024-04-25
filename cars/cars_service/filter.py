from dataclasses import dataclass, field
from cars.model import Car
from typing import Callable
from collections import defaultdict


@dataclass
class FilterService:
    cars: list[Car] = field(default_factory=list[Car])

    def get_cars(self) -> list[Car]:
        return self.cars

    def add_cars(self, cars: list[Car]) -> None:
        if len(cars) == 0:
            pass
        self.get_cars().extend(cars)

    def filter_cars(self, filter_fn: Callable[[Car], bool]) -> list[Car]:
        """
        Filters cars based on a provided filter function.

        Parameters:
            filter_fn (Callable[[Car], bool]): A function that takes a Car object and returns a boolean value.

        Returns:
            list[Car]: A list of cars that satisfy the filter function.
        """

        return [car for car in self.cars if filter_fn(car)]

    def get_cars_with_higher_mileage_than(self, mileage_limit: int) -> list[Car]:
        """
        Gets cars with mileage higher than a specified limit.

        Parameters:
            mileage_limit (int): The mileage limit to compare against.

        Returns:
            list[Car]: A list of cars with mileage higher than the specified limit.
        """

        return self.filter_cars(lambda car: car.has_mileage_higher_than(mileage_limit))

    def get_cars_with_price_between(self, min_price: int, max_price: int) -> list[Car]:
        """
        Gets cars with price within a specified range.

         Parameters:
             min_price (int): The minimum price.
             max_price (int): The maximum price.

         Returns:
             list[Car]: A list of cars with price within the specified range, sorted by model.
         """

        matching_cars = self.filter_cars(lambda car: car.has_price_between(min_price, max_price))
        return sorted(matching_cars, key=lambda car: car.model)

    def get_extreme_priced_cars(self, extreme_fn: Callable[[list[int]], int]) -> Car | list[Car]:
        """
        Gets cars with extreme prices based on a provided extreme function.

         Parameters:
             extreme_fn (Callable[[list[int]], int]): A function that takes a list of prices
              and returns an extreme value.

         Returns:
             Car | list[Car]: A single car or a list of cars with extreme prices.
         """

        grouped_by_price = defaultdict(list)
        for car in self.cars:
            grouped_by_price[car.price].append(car)

        extreme_value = extreme_fn(list(grouped_by_price.keys()))
        result = grouped_by_price[extreme_value]
        return result[0] if len(result) == 1 else result
