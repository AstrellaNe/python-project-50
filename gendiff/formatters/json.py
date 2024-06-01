import json


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


def handle_status(full_path, sorted_values, formatted_diff):
    status = sorted_values['status']
    if status == 'nested':
        formatted_diff.update(handle_nested(full_path, sorted_values))
    elif status == 'added':
        formatted_diff.update(handle_added(full_path, sorted_values))
    elif status == 'removed':
        formatted_diff.update(handle_removed(full_path))
    elif status == 'changed':
        formatted_diff.update(handle_changed(full_path, sorted_values))
    elif status is None:
        raise ValueError(f"Unknown status: {status}")


def handle_nested(full_path, sorted_values):
    return {
        full_path: {
            'status': 'nested',
            'children': format_json(sorted_values['children'], full_path)
        }
    }


def handle_added(full_path, sorted_values):
    return {
        full_path: {
            'status': 'added',
            'value': stringify(sorted_values['value'])
        }
    }


def handle_removed(full_path):
    return {
        full_path: {
            'status': 'removed'
        }
    }


def handle_changed(full_path, sorted_values):
    old_value = stringify(sorted_values['old_value'])
    new_value = stringify(sorted_values['new_value'])
    return {
        full_path: {
            'status': 'changed',
            'old_value': old_value,
            'new_value': new_value
        }
    }


def format_json(diff, path=''):
    formatted_diff = {}
    for key, sorted_values in sorted(diff.items()):
        full_path = f"{path}.{key}" if path else key
        handle_status(full_path, sorted_values, formatted_diff)
    return formatted_diff


def format_tree(diff):
    formatted_diff = format_json(diff)
    if not formatted_diff:
        return '{}'
    return json.dumps(formatted_diff, indent=4)
