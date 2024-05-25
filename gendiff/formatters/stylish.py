def stringify(value, depth):
    """Преобразует значение в строку с учетом глубины вложенности."""
    if isinstance(value, dict):
        return format_dict(value, depth)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_dict(value, depth):
    """Форматирует словарь с учетом глубины вложенности."""
    if not value:
        return '{}'
    lines = []
    indent = ' ' * (depth * 4)
    for key, val in value.items():
        lines.append(f"{indent}    {key}: {stringify(val, depth + 1)}")
    closing_indent = ' ' * (depth * 4)
    return '{\n' + '\n'.join(lines) + f'\n{closing_indent}}}'


def format_line(key, value, depth, status):
    """Форматирует строку с учетом статуса изменения."""
    base_indent = ' ' * (depth * 4 - 2)
    symbol = '  '  # Пробелы для неизмененных элементов
    if status == 'added':
        symbol = '+ '
    elif status == 'removed':
        symbol = '- '

    if status == 'nested':
        formatted_value = format_diff(value['children'], depth + 1)
        return (f"{base_indent}{symbol}{key}: {{\n"
                f"{formatted_value}\n{base_indent}  }}")
    else:
        formatted_value = stringify(value, depth)
        return f"{base_indent}{symbol}{key}: {formatted_value}"


def format_diff(diff, depth=1):
    """Формирует отформатированное представление различий."""
    lines = []
    for key, value in sorted(diff.items()):
        status = value.get('status')
        if status in ['added', 'removed', 'unchanged']:
            lines.append(format_line(key, value['value'], depth, status))
        elif status == 'changed':
            lines.append(format_line(key, value['old_value'], depth, 'removed'))
            lines.append(format_line(key, value['new_value'], depth, 'added'))
        else:  # 'nested'
            lines.append(format_line(key, value, depth, 'nested'))
    return '\n'.join(lines)


def _format_tree(diff):
    """Возвращает строковое представление дерева различий."""
    return '{\n' + format_diff(diff, 1) + '\n}'
