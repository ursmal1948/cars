from dataclasses import dataclass, field


@dataclass
class Car:
    model: str
    price: int
    color: str
    mileage: int
    components: list[str] = field(default_factory=list[str])

    def has_color(self, expected_color: str) -> bool:
        return self.color == expected_color

    def has_model(self, expected_model: str) -> bool:
        return self.model == expected_model

    def has_component(self, expected_component: str) -> bool:
        return expected_component in self.components

    def has_price_between(self, min_price: int, max_price: int) -> bool:
        if min_price > max_price:
            raise ValueError(f'Price range is not correct: [{min_price} ,{max_price}]')
        return min_price <= self.price <= max_price
