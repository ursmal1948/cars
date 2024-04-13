import logging

from cars.model import Car
from cars.file.service import FromTxtFileToCar, FromJsonFileToCar
from cars.file.service import DataProcessor


class TestDataProcessor:
    def test_text_data_processor(self, txt_path_correct_data):
        txt_data_factory = FromTxtFileToCar()
        processor = DataProcessor(txt_data_factory)
        cars = processor.process(txt_path_correct_data, None)
        assert cars == [
            Car(model='BMW', price=2000, color='BLUE', mileage=1500, components=['BLUETOOTH', 'ABS'])
        ]

    def test_json_data_processor(self, json_path_correct_data):
        json_data_factory = FromJsonFileToCar()
        processor = DataProcessor(json_data_factory)
        cars = processor.process(json_path_correct_data, 'cars')

        assert cars == [
            Car(model='AUDI', price=9000, color='SILVER', mileage=1500, components=['CAMERA']),
            Car(model='TOYOTA', price=4000, color='BLUE', mileage=10000, components=['KEYLESS ENTRY', 'BLUETOOTH'])

        ]
