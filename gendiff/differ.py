import json
import yaml
from typing import Any, Dict, Optional
from gendiff.loader import load_file  # Импорт загрузки файла
from gendiff.formatters.stylish import _format_tree as format_stylish
from gendiff.formatters.plain import _format_tree as format_plain


# 80 знаков в линтере - это извращение!!!!!
def generate_diff(file_path1: str, file_path2: str,
                  format_name: str = 'stylish') -> Optional[str]:
    try:
        data1 = load_file(file_path1)
        data2 = load_file(file_path2)
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e.filename}")
        return None
    except (json.JSONDecodeError, yaml.YAMLError, ValueError) as e:
        print(f"Ошибка при обработке файла: {e}")
        return None

    # Создается диффер без форматирования
    structured_diff = create_diff(data1, data2)

    # Применяем форматтер
    if format_name == 'plain':
        return format_plain(structured_diff)
    elif format_name == 'stylish':
        return format_stylish(structured_diff)
    else:
        print(f"Ошибка: Неизвестный формат '{format_name}'")
        return None


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
