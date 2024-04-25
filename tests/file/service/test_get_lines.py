import pytest
from cars.file.reader import JsonFileService
from cars.file.reader import TxtFileService


class TestJsonFileServiceGetLines:
    def test_when_path_has_incorrect_extension(self):
        with pytest.raises(AttributeError) as e:
            JsonFileService().get_lines('test_data/cars_test.png', 'key')
        assert str(e.value) == 'File has incorrect extension'

    def test_when_path_not_found(self):
        with pytest.raises(FileNotFoundError) as e:
            JsonFileService().get_lines('test_data/cars_testt.json', 'key')
        assert str(e.value).startswith('File not found')

    def test_when_key_not_found(self, json_path_correct_data):
        with pytest.raises(AttributeError) as e:
            JsonFileService().get_lines(json_path_correct_data, 'people')
        assert str(e.value).startswith('Key not found')

    def test_when_file_has_no_content(self):
        data = JsonFileService().get_lines('test_data/empty_cars_test.json', 'cars')
        assert len(data) == 0

    def test_when_content_present(self, json_path_correct_data):
        data = JsonFileService().get_lines(json_path_correct_data, 'cars')
        assert len(data) == 3
        assert list(data[0].values()) == ['AUDI', 9000, 'SILVER', 1500, ['CAMERA']]
        assert list(data[1].values()) == ['BMW', 3000, 'WHITE', 2800, ['KEYLESS ENTRY']]
        assert list(data[2].values()) == ['TOYOTA', 4000, 'BLUE', 10000, ['KEYLESS ENTRY', 'BLUETOOTH']]


class TestTxtFileServiceGetLinesPathNotCorrect:

    def test_when_path_has_incorrect_extension(self):
        with pytest.raises(AttributeError) as e:
            TxtFileService().get_lines('test_data/cars_test.jpg')
        assert str(e.value).startswith('File has incorrect extension')

    def test_when_path_not_found(self):
        with pytest.raises(FileNotFoundError) as e:
            TxtFileService().get_lines('test_data/cars_testt.txt')
        assert str(e.value).startswith('File not found')

    def test_when_file_has_no_content(self):
        content = TxtFileService().get_lines('test_data/empty_cars_test.txt')
        assert content == []

    def test_when_file_has_wrong_content(self):
        with pytest.raises(ValueError) as e:
            TxtFileService().get_lines('test_data/wrong_content_cars_test.txt')
        assert str(e.value).startswith('Error parsing line')

    def test_when_content_present(self, txt_path_correct_data):
        content = TxtFileService().get_lines(txt_path_correct_data)
        assert len(content) == 2
        assert list(content[0].values()) == ['BMW', 2000, 'BLUE', 1500, ['BLUETOOTH', 'ABS']]
        assert list(content[1].values()) == ['OPEL', 1000, 'SILVER', 2000, ['CAMERA', 'ABS']]
