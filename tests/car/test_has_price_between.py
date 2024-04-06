class TestCarHasPriceBetween:

    def test_when_car_has_price_between(self, test_car_example):
        assert test_car_example.has_price_between(200, 300)
        assert test_car_example.has_price_between(100, 300)
        assert test_car_example.has_price_between(100, 200)

    def test_when_car_has_not_price_between(self, test_car_example):
        assert not test_car_example.has_price_between(10, 20)
