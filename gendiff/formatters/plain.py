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


def format_plain(diff, path=''):
    lines = []
    for key, sorted_values in sorted(diff.items()):
        full_path = f"{path}.{key}" if path else key
        status = sorted_values['status']

        if status == 'nested':
            lines.append(format_plain(sorted_values['children'], full_path))
        elif status == 'added':
            value = stringify(sorted_values['value'])
            lines.append(
                f"Property '{full_path}' was added with value: "
                f"{value}"
            )
        elif status == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif status == 'changed':
            old_value = stringify(sorted_values['old_value'])
            new_value = stringify(sorted_values['new_value'])
            lines.append(
                f"Property '{full_path}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return '\n'.join(filter(None, lines))


def _format_tree(diff):
    return format_plain(diff)
