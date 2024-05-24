import json


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return value
    else:
        return value


def format_json(diff, path=''):
    formatted_diff = {}

    for key, sorted_values in sorted(diff.items()):
        full_path = f"{path}.{key}" if path else key
        status = sorted_values['status']

        if status == 'nested':
            formatted_diff[full_path] = {
                'status': 'nested',
                'children': format_json(sorted_values['children'], full_path)
            }
        elif status == 'added':
            value = stringify(sorted_values['value'])
            formatted_diff[full_path] = {
                'status': 'added',
                'value': value
            }
        elif status == 'removed':
            formatted_diff[full_path] = {
                'status': 'removed'
            }
        elif status == 'changed':
            old_value = stringify(sorted_values['old_value'])
            new_value = stringify(sorted_values['new_value'])
            formatted_diff[full_path] = {
                'status': 'changed',
                'old_value': old_value,
                'new_value': new_value
            }

    return formatted_diff


def _format_tree(diff):
    formatted_diff = format_json(diff)
    return json.dumps(formatted_diff, indent=4)
