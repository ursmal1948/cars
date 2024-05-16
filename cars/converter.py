from abc import ABC, abstractmethod
from typing import Any
from cars.model import Car


class AsyncConverter(ABC):
    @abstractmethod
    async def convert(self, data: list[dict[str, Any]]) -> list[Car]:
        pass


class AsyncCarsConverter(AsyncConverter):
    async def convert(self, data: list[dict[str, Any]]) -> list[Car]:
        return [await Car.from_dict(car) for car in data]
