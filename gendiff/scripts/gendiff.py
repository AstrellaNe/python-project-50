import argparse
from gendiff.differ import generate_diff
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
    parser.add_argument('-f', '--format',
                        choices=['stylish', 'plain'], default='stylish',
                        help='формат вывода'
                        ' по умолчанию: "stylish"')
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Generate and format the diff
    formatted_diff = generate_diff(args.file_path1, args.file_path2,
                                   args.format)

    if formatted_diff is None:
        print("Ошибка: Не удалось сгенерировать различия между файлами."
              "Проверьте пути и доступность файлов.")
    else:
        print(formatted_diff)


if __name__ == '__main__':
    main()
