#!/usr/bin/env python3

import argparse
import json
import sys
from typing import Any, Dict


def _load_json_file(file_path: str) -> Dict:
    """
       Загружает и возвращает данные из JSON-файла.
       Обрабатываем ошибки сразу. Потом можно добавить еще.
       Функция неявная, чтобы защитить использование файлов.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {file_path}.")
        return {}


def _compare_values(value1: Any, value2: Any) -> Dict[str, Any]:
    """Возвращает словарь c результатом сравнения двух значений."""
    if value1 == value2:
        return {'status': 'unchanged', 'value': value1}
    return {'status': 'changed', 'old_value': value1, 'new_value': value2}


def generate_diff(file_path1: str, file_path2: str) -> str:
    data1, data2 = _load_json_file(file_path1), _load_json_file(file_path2)
    if data1 is None or data2 is None:
        return  # Если один из файлов не найден - не продолжаем.

    return format_diff(_create_diff(data1, data2))


def _create_diff(data1: Dict, data2: Dict) -> Dict[str, Dict[str, Any]]:
    """Создает и возвращает словарь различий между двумя словарями."""
    diff = {}  # пустой словарь для хранения результатов сравнения.
    all_keys = set(data1) | set(data2)

    for key in all_keys:
        diff[key] = _get_key_diff(data1, data2, key)

    return diff


def _get_key_diff(data1: Dict, data2: Dict, key: str) -> Dict[str, Any]:
    """Возвращает различие для конкретного ключа между двумя словарями."""
    if key in data1 and key in data2:
        return _compare_values(data1[key], data2[key])
    elif key in data1:
        return {'status': 'removed', 'value': data1[key]}
    elif key in data2:
        return {'status': 'added', 'value': data2[key]}


def format_diff(diff: Dict[str, Dict[str, Any]]) -> str:
    """
       Вспомогательная функция
       Форматирует различия в удобочитаемую строку.
    """
    lines = []  # список строк, который хранит отформатированные различия.

    # Перебираем отсортированные по ключам элементы словаря различий.
    for key, details in sorted(diff.items()):
        # статус различия текущего ключа (добав., удал., изм.)
        status = details['status']

        # format_change для получения строк описания изменений
        # добавляем их в список строк.
        lines.extend(format_change(key, details, status))

    # Соединяем все строки из списка в одну строку, обрамляем скобками под JS.
    # Каждая строка переносится.
    return ('{\n' + '\n'.join(lines) + '\n}')


def format_change(key: str, details: Dict[str, Any], status: str) -> list:
    """Возвращает список строк, описывающих изменение для одного ключа."""
    change_lines = []  # список для хранения измененных строк.

    # в зависимости от статуса - добавляет соответв. строки в change_lines.
    if status == 'unchanged':
        change_lines.append(f'  {key}: {details["value"]}')
    elif status == 'changed':
        change_lines.append(f'- {key}: {details["old_value"]}')
        change_lines.append(f'+ {key}: {details["new_value"]}')
    elif status == 'removed':
        change_lines.append(f'- {key}: {details["value"]}')
    elif status == 'added':
        change_lines.append(f'+ {key}: {details["value"]}')

    # возвращаем видоизмененные строки
    return change_lines


# Отладка
# def main():
    file1 = 'fil67e1.json'
    file2 = 'fil32.json'
    diff = generate_diff(file1, file2)
    print(diff)
    file1 = 'file1.json'
    file2 = 'file2.json'
    diff = generate_diff(file1, file2)
    print(diff)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='first file to compare')
    parser.add_argument('second_file', help='second file to compare')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')

    args = parser.parse_args()
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    # Проверяем, предоставлены ли оба файла перед выполнением сравнения
    if args.first_file is None or args.second_file is None:
        parser.print_usage()  # краткая справка, если файлы не указаны
        sys.exit(1)

    diff = generate_diff(file1, file2)
    if diff is not None:
        print(diff)


if __name__ == '__main__':
    main()
