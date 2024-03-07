import argparse
# отдельный модуль для парсера по заданию


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Сравнивает два файла конфигурации и показывает разницу.')
    parser.add_argument('first_file', help='первый файл для сравнения')
    parser.add_argument('second_file', help='второй файл для сравнения')
    return parser.parse_args()
