#!/usr/bin/env python3

import argparse
import json
# import sys
import yaml  # Импортируем библиотеку yaml
from typing import Any, Dict, Optional


def _load_file(file_path: str) -> Optional[Dict]:
    """
    Загружает и возвращает данные из файла JSON или YAML
    в зависимости от расширения файла и корректно обрабатывает ошибки.
    Функция объявлена как приватная для ограничения использования файлов.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if file_path.endswith('.json'):
                return json.load(file)
            elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
                return yaml.safe_load(file)
            else:
                print(f"Неподдерживаемый тип файла: {file_path}")
                return None
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"Ошибка при декодировании файла {file_path}: {e}")
        return None


def _compare_values(value1: Any, value2: Any) -> Dict[str, Any]:
    """Возвращает словарь с результатами сравнения двух значений."""
    if value1 == value2:
        return {'status': 'unchanged', 'value': value1}
    return {'status': 'changed', 'old_value': value1, 'new_value': value2}


def generate_diff(file_path1: str, file_path2: str) -> Optional[str]:
    data1, data2 = _load_file(file_path1), _load_file(file_path2)
    if data1 is None or data2 is None:
        return None
    # Если один из файлов загружен некорректно, прерываем выполнение.

    return format_diff(_create_diff(data1, data2))


def _create_diff(data1: Dict, data2: Dict) -> Dict[str, Dict[str, Any]]:
    """Создает и возвращает словарь различий между двумя словарями."""
    diff = {}
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
    """Форматирует различия в строку, удобную для чтения человеком."""
    lines = []
    for key, details in sorted(diff.items()):
        status = details['status']
        lines.extend(format_change(key, details, status))
    return '{\n' + '\n'.join(lines) + '\n}'


def format_change(key: str, details: Dict[str, Any], status: str) -> list:
    """Возвращает список строк, описывающих изменения для одного ключа."""
    change_lines = []
    if status == 'unchanged':
        change_lines.append(f'  {key}: {details["value"]}')
    elif status == 'changed':
        change_lines.append(f'- {key}: {details["old_value"]}')
        change_lines.append(f'+ {key}: {details["new_value"]}')
    elif status == 'removed':
        change_lines.append(f'- {key}: {details["value"]}')
    elif status == 'added':
        change_lines.append(f'+ {key}: {details["value"]}')
    return change_lines


def main():
    parser = argparse.ArgumentParser(
        description='Сравнивает два файла конфигурации и показывает разницу.')
    parser.add_argument('first_file', help='первый файл для сравнения')
    parser.add_argument('second_file', help='второй файл для сравнения')
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    if diff:
        print(diff)


if __name__ == '__main__':
    main()
