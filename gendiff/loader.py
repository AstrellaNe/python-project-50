import json
import yaml
from typing import Any, Dict


def load_file(file_path: str) -> Dict[Any, Any]:
    """
    Загружает и возвращает данные из файла JSON или YAML
    в зависимости от расширения файла.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith(('.yaml', '.yml')):
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {file_path}")
