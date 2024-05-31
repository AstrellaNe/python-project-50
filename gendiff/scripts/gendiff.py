import argparse
from gendiff.differ_engine import generate_diff
# Перенес импорт форматтеров в differ.py
# Здесь происходит только обработка ком. строки


def parse_arguments():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Создает различия между двумя \
файлами')
    # Добавляем аргументы для путей к файлам в хэлп
    parser.add_argument('file_path1', type=str, help='путь к первому файлу')
    parser.add_argument('file_path2', type=str, help='путь ко второму файлу')
    # Выбора форматтера
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='формат вывода (stylish, plain, json),'
                        ' по умолчанию "stylish" ')
    return parser.parse_args()


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')

    args = parser.parse_args()

    try:
        diff = generate_diff(args.first_file, args.second_file,
                             args.format)
        if diff is not None:
            print(diff)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
