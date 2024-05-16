from cars.file.service import DataProcessor, DataFactoryType, FromJsonFileToCar, FromTxtFileToCar


def main() -> None:
    from_txt_file = FromTxtFileToCar()
    processor = DataProcessor(from_txt_file)
    res = processor.process('test_data/cars_test.txt')
    processor2 = processor.create_processor(DataFactoryType.FROM_JSON)
    res2 = processor2.process('test_data/cars_test.json', 'cars')
    print(res)
    print(res2)


if __name__ == '__main__':
    main()
