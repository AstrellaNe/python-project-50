def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


# Рефактор функций чтобы снизить complexity (линтер - зло!!!)
def handle_nested(diff, full_path):
    return format_plain(diff, full_path)


def handle_added(full_path, sorted_values):
    value = stringify(sorted_values['value'])
    return f"Property '{full_path}' was added with value: {value}"


def handle_removed(full_path):
    return f"Property '{full_path}' was removed"


def handle_changed(full_path, sorted_values):
    old_value = stringify(sorted_values['old_value'])
    new_value = stringify(sorted_values['new_value'])
    return (f"Property '{full_path}' was updated. "
            f"From {old_value} to {new_value}")


def handle_status(full_path, sorted_values):
    status = sorted_values['status']
    if status == 'nested':
        return handle_nested(sorted_values['children'], full_path)
    elif status == 'added':
        return handle_added(full_path, sorted_values)
    elif status == 'removed':
        return handle_removed(full_path)
    elif status == 'changed':
        return handle_changed(full_path, sorted_values)
    elif status == 'unchanged':
        return None
    else:
        raise ValueError(f"Unknown status: {status}")


def format_plain(diff, path=''):
    lines = []
    for key, sorted_values in sorted(diff.items()):
        full_path = f"{path}.{key}" if path else key
        result = handle_status(full_path, sorted_values)
        if result:
            lines.append(result)

    return '\n'.join(filter(None, lines))


def format_tree(diff):
    return format_plain(diff)
