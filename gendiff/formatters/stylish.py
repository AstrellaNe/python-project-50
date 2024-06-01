def stringify(value, depth):
    """Преобразует значение в строку с учетом глубины вложенности."""
    if isinstance(value, dict):
        return format_dict(value, depth)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
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


def format_diff(diff, depth=1):
    """Формирует отформатированное представление различий."""
    lines = []
    for key, value in sorted(diff.items()):
        lines.append(format_node(key, value, depth))
    return '\n'.join(lines)


def format_node(key, value, depth):
    """Форматирует узел в зависимости от его статуса."""
    status = value.get('status')
    if status in ['added', 'removed', 'unchanged']:
        return format_line(key, value['value'], depth, status)
    elif status == 'changed':
        return format_changed_node(key, value, depth)
    elif status == 'nested':
        return format_line(key, value, depth, 'nested')
    else:
        raise ValueError(f"Unknown status: {status}")


def format_changed_node(key, value, depth):
    """Форматирует измененный узел (added и removed)."""
    old_value = format_line(key, value['old_value'], depth, 'removed')
    new_value = format_line(key, value['new_value'], depth, 'added')
    return f"{old_value}\n{new_value}"


def format_line(key, value, depth, status):
    """Форматирует строку с учетом статуса изменения."""
    base_indent = ' ' * (depth * 4 - 2)
    symbol = get_symbol(status)

    if status == 'nested':
        formatted_value = format_diff(value['children'], depth + 1)
        return (f"{base_indent}{symbol}{key}: {{\n"
                f"{formatted_value}\n{base_indent}  }}")
    else:
        formatted_value = stringify(value, depth)
        return f"{base_indent}{symbol}{key}: {formatted_value}"


def get_symbol(status):
    """Возвращает символ для строки на основе статуса."""
    if status == 'added':
        return '+ '
    elif status == 'removed':
        return '- '
    return '  '


def format_tree(diff):
    """Возвращает строковое представление дерева различий."""
    return '{\n' + format_diff(diff, 1) + '\n}'
