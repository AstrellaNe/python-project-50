import json
import yaml
from typing import Any, Dict, Optional
from gendiff.loader import load_file  # Импорт загрузки файла


def generate_diff(file_path1: str, file_path2: str) -> Optional[Dict[str, Any]]:
    try:
        data1 = load_file(file_path1)
        data2 = load_file(file_path2)
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e.filename}")
        return None
    except (json.JSONDecodeError, yaml.YAMLError, ValueError) as e:
        print(f"Ошибка при обработке файла: {e}")
        return None
    return create_diff(data1, data2)


def create_diff(data1, data2):
    diff = {}
    all_keys = sorted(data1.keys() | data2.keys())

    for key in all_keys:
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff[key] = {'status': 'nested', 'children':
                             create_diff(data1[key], data2[key])}
                #  присваиваем 'nested'
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
