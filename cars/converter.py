from abc import ABC, abstractmethod
from typing import Any
from cars.model import Car


class Converter(ABC):
    @abstractmethod
    def convert(self, data: list[dict[str, Any]]) -> list[Car]:
        pass


class CarsConverter(Converter):
    def convert(self, data: list[dict[str, Any]]) -> list[Car]:
        return [Car.from_dict(car) for car in data]
