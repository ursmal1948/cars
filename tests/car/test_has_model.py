class TestCarHasModel:

    def test_when_car_has_model(self, test_car_example):
        assert test_car_example.has_model('HONDA')

    def test_when_car_has_not_model(self, test_car_example):
        assert not test_car_example.has_model('BMW')
