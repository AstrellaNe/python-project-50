import json
import yaml
from typing import Any, Dict, Optional
from gendiff.loader import read_file
from gendiff.formatters.stylish import format_tree as format_stylish
from gendiff.formatters.plain import format_tree as format_plain
from gendiff.formatters.json import format_tree as format_json


def load_data(file_path1: str, file_path2: str) -> Optional[Dict[str, Any]]:
    try:
        data1 = read_file(file_path1)
        data2 = read_file(file_path2)
        return {'data1': data1, 'data2': data2}
    except FileNotFoundError as e:
        raise ValueError(f"Ошибка: файл не найден - {e.filename}") from e
    except (json.JSONDecodeError, yaml.YAMLError, ValueError) as e:
        raise ValueError(f"Ошибка при обработке файла: {e}") from e
# Вместо вывода сообщения об ошибке в стандартные потоки ввода/вывода,
# теперь везде поднимает исключение ValueError с соответствующим сообщением.


def apply_formatter(diff: Dict[str, Any], format_name: str) -> Optional[str]:
    if format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Ошибка: Неизвестный формат '{format_name}'")


def generate_diff(file_path1: str, file_path2: str,
                  format_name: str = 'stylish') -> Optional[str]:
    data = load_data(file_path1, file_path2)
    if data is None:
        return None

    structured_diff = create_diff(data['data1'], data['data2'])
    return apply_formatter(structured_diff, format_name)


def create_diff(data1: Dict[str, Any], data2: Dict[str, Any]) -> Dict[str, Any]:
    diff = {}
    all_keys = sorted(data1.keys() | data2.keys())

    for key in all_keys:
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff[key] = {'status': 'nested',
                             'children': create_diff(data1[key], data2[key])}
            elif data1[key] == data2[key]:
                diff[key] = {'status': 'unchanged', 'value': data1[key]}
            else:
                diff[key] = {'status': 'changed', 'old_value': data1[key],
                             'new_value': data2[key]}
        elif key in data1:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        else:
            diff[key] = {'status': 'added', 'value': data2[key]}
    return diff
