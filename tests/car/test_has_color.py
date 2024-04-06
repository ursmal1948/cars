from cars.model import Car


class TestCarHasColor:

    def test_when_car_has_expected_color(self, test_car_example):
        assert test_car_example.has_color('BLUE')

    def test_when_car_has_not_expected_color(self, test_car_example):
        assert not test_car_example.has_color('WHITE')
