def get_plain(data, path=''):
    result = []
    for entry in data:
        key = entry['key']
        if entry['status'] == 'deleted':
            result.append(
                f"Property '{path}{key}' was removed"
            )
        elif entry['status'] == 'added':
            value = normalize(entry['value'])
            result.append(
                f"Property '{path}{key}' was added with value: {value}"
            )
        elif entry['status'] == 'changed':
            value1 = normalize(entry['value1'])
            value2 = normalize(entry['value2'])
            result.append(
                f"Property '{path}{key}' was updated. "
                f"From {value1} to {value2}"
            )
        elif entry['status'] == 'parent':
            children = entry['children']
            result.append(
                get_plain(children, path=path + f'{key}.')
            )

    return '\n'.join(result)


def normalize(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return str(value)
    else:
        return f"'{value}'"
