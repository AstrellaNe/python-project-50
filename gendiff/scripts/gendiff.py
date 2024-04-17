import argparse
from gendiff.differ import generate_diff
from gendiff.formatters.stylish import _format_tree as format_stylish
from gendiff.formatters.plain import _format_tree as format_plain


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('file_path1', type=str, help='path to first file')
    parser.add_argument('file_path2', type=str, help='path to second file')
    parser.add_argument('-f', '--format',
                        choices=['stylish', 'plain'], default='stylish',
                        help='set format of output (default: "stylish")')
    return parser.parse_args()


def main():
    # Парсинг аргументов командной строки
    args = parse_arguments()

    diff = generate_diff(args.file_path1, args.file_path2)

    if diff is None:
        print("Ошибка: Не удалось сгенерировать различия между файлами. "
              "Проверьте пути и доступность файлов.")
        return

    # Форматирование различий в зависимости от выбранного формата
    if args.format == 'plain':
        formatted_diff = format_plain(diff)
    else:  # По умолчанию используется формат "stylish"
        formatted_diff = format_stylish(diff)

    print(formatted_diff)


if __name__ == '__main__':
    main()
