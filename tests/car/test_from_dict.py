from cars.model import Car


class TestCarFromDict:

    def test(self, test_car_example):
        data = {
            "model": "HONDA",
            "price": 200,
            "color": "BLUE",
            "mileage": 200,
            "components": ["ABS", "AIR CONDITIONING"]}
        actual_car = Car.from_dict(data)
        assert actual_car == test_car_example
