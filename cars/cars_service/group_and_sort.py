from dataclasses import dataclass
from collections import defaultdict, Counter
from typing import Callable
from functools import cmp_to_key
from cars.cars_service.service import CarsService
from cars.model import Car


@dataclass
class GroupAndSortService(CarsService):

    def sort_cars(self, sort_fn: Callable[[Car, Car], bool]) -> list[Car]:
        return sorted(self.cars, key=cmp_to_key(sort_fn))

    @staticmethod
    def compare_cars(car1: Car, car2: Car, sorting_key: str) -> int:
        key_value1 = getattr(car1, sorting_key)
        key_value2 = getattr(car2, sorting_key)

        if key_value1 == key_value2:
            return 0
        elif key_value1 < key_value2:
            return -1
        else:
            return 1

    def sort_by(self, sorting_key: str) -> list[Car]:
        if not all(hasattr(car, sorting_key) for car in self.cars):
            raise AttributeError('Incorrect key')
        return self.sort_cars(sort_fn=lambda car1, car2: self.compare_cars(car1, car2, sorting_key))

    def group_by_color(self) -> dict[str, int]:
        """
        Groups cars by their colors and counts the occurrences of each color.

        Returns:
            dict[str, int]: A dictionary where keys are car colors and values are the number of cars with
            each color.
        """

        cnt = Counter()
        for car in self.cars:
            cnt[car.color] += 1
        return dict(sorted(cnt.items(), key=lambda e: e[1], reverse=True))

    def get_most_expensive_car_for_model(self, model: str) -> Car | list[Car]:
        """
        Retrieves the most expensive car(s) for the given model.

        Parameters:
           model (str): The model of the car for which to find the most expensive one(s).

        Returns:
            Car | list[Car]: If there's only one most expensive car for the given model, it returns that car.
                             If there are multiple cars with the same highest price, it returns a list containing
                             all of them. If there are no cars for the given model, it returns an empty list.
        """

        grouped_by_price = defaultdict(list)
        for car in self.cars:
            if car.model == model:
                grouped_by_price[car.price].append(car)
        if not grouped_by_price:
            return []
        most_expensive = max(grouped_by_price.keys())
        result = grouped_by_price[most_expensive]
        return result if len(result) > 1 else result[0]

    def group_most_expensive_cars_by_model(self) -> dict[str, list[Car]]:
        """
        Groups the most expensive car/cars for each model.

        Returns:
            dict[str, list[Car]]: A dictionary where keys are car models and values are lists containing
            the most expensive car/cars for each model.
        """

        most_expensive_car_by_model = defaultdict(list)
        unique_models = set(car.model for car in self.cars)
        for model in unique_models:
            most_expensive_car_by_model[model] = self.get_most_expensive_car_for_model(model)
        return dict(sorted(most_expensive_car_by_model.items(), key=lambda e: [0]))

    def group_cars_by_component(self) -> dict[str, list[Car]]:
        """
        Groups cars by their components.

        Returns:
            dict[str, list[Car]]: A dictionary where keys are car components and values are lists containing
            the cars having that component.
        """

        unique_components = set(car.component for car in self.cars for car.component in car.components)
        return {component: [car for car in self.cars if car.has_component(component)] for component in
                unique_components}
