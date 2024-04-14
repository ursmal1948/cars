import pytest
from cars.file.reader import TxtFileService


class TestTxtFileServiceGetLinesPathNotCorrect:

    def test_when_path_has_incorrect_extension(self):
        with pytest.raises(AttributeError) as e:
            TxtFileService().get_lines('test_data/cars_test.jpg')
        assert str(e.value).startswith('File has incorrect extension')

    def test_when_path_not_found(self):
        with pytest.raises(FileNotFoundError) as e:
            TxtFileService().get_lines('test_data/cars_testt.txt')
        assert str(e.value).startswith('File not found')


class TestTxtFileServiceGetLinesEmptyContent:
    def test_when_file_has_no_content(self):
        content = TxtFileService().get_lines('test_data/empty_cars_test.txt')
        assert content == []


class TestTxtFileServiceWrongContent:
    def test_when_file_has_wrong_content(self):
        with pytest.raises(ValueError) as e:
            TxtFileService().get_lines('test_data/wrong_content_cars_test.txt')
        assert str(e.value).startswith('Error parsing line')


class TestTxtFileServiceCorrectContent:
    def test_when_content_present(self,txt_path_correct_data):
        content = TxtFileService().get_lines(txt_path_correct_data)
        assert len(content) == 2
        assert list(content[0].values()) == ['BMW', 2000, 'BLUE', 1500, ['BLUETOOTH', 'ABS']]
        assert list(content[1].values()) == ['OPEL', 1000, 'SILVER', 2000, ['CAMERA', 'ABS']]
