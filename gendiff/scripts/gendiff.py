import argparse
import json
import yaml
from gendiff.differ_engine import generate_diff


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
    try:
        args = parse_arguments()
        diff = generate_diff(args.file_path1, args.file_path2, args.format)
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e.filename}")
        return
    except (json.JSONDecodeError, yaml.YAMLError, ValueError) as e:
        print(f"Ошибка при обработке файла: {e}")
        return

    if diff is not None:
        print(diff)


if __name__ == '__main__':
    main()
