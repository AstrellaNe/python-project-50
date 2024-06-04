from typing import Any, Dict, Optional
from .stylish import format_tree as format_stylish
from .plain import format_tree as format_plain
from .json import format_tree as format_json


def apply_formatter(diff: Dict[str, Any], format_name: str) -> Optional[str]:
    if format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Ошибка: Неизвестный формат '{format_name}'")
