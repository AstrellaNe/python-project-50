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

    diff = {}  # пустой словарь для хранения результатов сравнения.

    # Создаем множество уникальных ключей из обоих словарей.
    for key in set(data1) | set(data2):
        # Если ключ в обоих словарях
        if key in data1 and key in data2:
            diff[key] = _compare_values(data1[key], data2[key])
        # Если только в первом словаре - помечаем как удаленный.
        elif key in data1:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        # Если во втором словаре, помечаем как добавленный.
        else:
            diff[key] = {'status': 'added', 'value': data2[key]}

    # Форматируем словарь различий в строку для вывода.
    return format_diff(diff)


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
    if status == 'unchanged':
        return [f'  {key}: {details["value"]}']
    elif status == 'changed':
        return [f'- {key}: {details["old_value"]}',
                f'+ {key}: {details["new_value"]}']
    elif status == 'removed':
        return [f'- {key}: {details["value"]}']
    elif status == 'added':
        return [f'+ {key}: {details["value"]}']

    return []


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
