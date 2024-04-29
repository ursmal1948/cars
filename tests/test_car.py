from cars.model import Car


class TestCarModel:
    def test_when_car_has_expected_model(self, test_car_example):
        assert test_car_example.has_model('HONDA')

    def test_when_car_has_not_expected_model(self, test_car_example):
        assert not test_car_example.has_model('BMW')

    def test_when_car_has_expected_color(self, test_car_example):
        assert test_car_example.has_color('BLUE')

    def test_when_car_has_not_expected_color(self, test_car_example):
        assert not test_car_example.has_color('WHITE')

    def test_when_car_has_expected_component(self, test_car_example):
        assert test_car_example.has_component('ABS')

    def test_when_car_has_not_expected_component(self, test_car_example):
        assert not test_car_example.has_component('BLUETOOTH')

    def test_when_car_has_price_between(self, test_car_example):
        assert test_car_example.has_price_between(200, 300)
        assert test_car_example.has_price_between(100, 300)
        assert test_car_example.has_price_between(100, 200)

    def test_when_car_has_not_price_between(self, test_car_example):
        assert not test_car_example.has_price_between(10, 20)


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
