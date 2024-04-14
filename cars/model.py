from dataclasses import dataclass, field
from typing import Any, Self


@dataclass
class Car:
    model: str
    price: int
    color: str
    mileage: int
    components: list[str] = field(default_factory=list[str])

    def has_color(self, expected_color: str) -> bool:
        """
        Checks if the car has the expected color.

        Parameters:
            expected_color (str): The expected color.

        Returns:
            bool: True if the car's color matches the expected color, False otherwise.
        """

        return self.color == expected_color

    def has_model(self, expected_model: str) -> bool:
        """
        Checks if the car has the expected model.

        Parameters:
            expected_model (str): The expected model.

        Returns:
            bool: True if the car's model matches the expected model, False otherwise.
        """

        return self.model == expected_model

    def has_component(self, expected_component: str) -> bool:
        """
        Checks if the car has a specific component.

         Parameters:
             expected_component (str): The component to check.

         Returns:
             bool: True if the car has the expected component, False otherwise.
         """

        return expected_component in self.components

    def has_price_between(self, min_price: int, max_price: int) -> bool:
        """
        Checks if the car's price falls within a specified range.

        Parameters:
            min_price (int): The minimum price.
            max_price (int): The maximum price.

        Returns:
            bool: True if the car's price falls within the specified range, False otherwise.

        Raises:
            ValueError: If the minimum price is greater than the maximum price.
        """

        if min_price > max_price:
            raise ValueError(f'Price range is not correct: [{min_price} ,{max_price}]')
        return min_price <= self.price <= max_price

    def has_mileage_higher_than(self, mileage_limit: int) -> bool:
        """
        Checks if the car's mileage is higher than a specified limit.

          Parameters:
              mileage_limit (int): The mileage limit to compare against.

          Returns:
              bool: True if the car's mileage is higher than the specified limit, False otherwise.
          """

        return self.mileage > mileage_limit

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """
        Creates a Car instance from a dictionary.

        Parameters:
            data (dict[str, Any]): A dictionary containing car data.

        Returns:
            Car: An instance of Car created from the provided dictionary.
        """
        return cls(**data)
