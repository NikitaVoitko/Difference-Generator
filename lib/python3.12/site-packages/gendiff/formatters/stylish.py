def get_stylish(data):
    return make_diff(data, depth=1)


def make_diff(current_data, depth):
    if not isinstance(current_data, (list, dict)):
        return str(current_data)
    lines = make_lines(current_data, depth)
    return '\n'.join(lines)


def make_lines(current_data, depth):
    indent = ' ' * 4 * depth
    closing_indent = ' ' * 4 * (depth - 1)
    lines = []

    if isinstance(current_data, dict):
        for k, v in current_data.items():
            lines.append(f'{indent}{k}: {make_diff(v, depth=depth + 1)}')
    for diff in current_data:
        add_lines(diff, depth, lines)

    result = ['{'] + lines + [closing_indent + '}']
    return result


def add_lines(diff, depth, lines):
    status = get_status(diff)
    if status == 'deleted':
        add_deleted(diff, depth, lines)
    elif status == 'added':
        add_added(diff, depth, lines)
    elif status == 'unchanged':
        add_unchanged(diff, depth, lines)
    elif status == 'changed':
        add_changed(diff, depth, lines)
    elif status == 'parent':
        add_parent(diff, depth, lines)
    return lines


def add_deleted(diff, depth, lines):
    indent = ' ' * ((4 * depth) - 2)
    value = normalize_value(diff['value'])
    key = '- ' + diff['key']
    lines.append(
        f'{indent}{key}: {make_diff(value, depth=depth + 1)}'
    )


def add_added(diff, depth, lines):
    indent = ' ' * ((4 * depth) - 2)
    value = normalize_value(diff['value'])
    key = '+ ' + diff['key']
    lines.append(
        f'{indent}{key}: {make_diff(value, depth=depth + 1)}'
    )


def add_unchanged(diff, depth, lines):
    indent = ' ' * 4 * depth
    value = normalize_value(diff['value'])
    key = diff['key']
    lines.append(
        f'{indent}{key}: {make_diff(value, depth=depth + 1)}'
    )


def add_changed(diff, depth, lines):
    indent = ' ' * ((4 * depth) - 2)
    value1 = normalize_value(diff['value1'])
    value2 = normalize_value(diff['value2'])
    key1 = '- ' + diff['key']
    key2 = '+ ' + diff['key']
    lines.append(
        f'{indent}{key1}: {make_diff(value1, depth=depth + 1)}'
    )
    lines.append(
        f'{indent}{key2}: {make_diff(value2, depth=depth + 1)}'
    )


def add_parent(diff, depth, lines):
    indent = ' ' * 4 * depth
    children = normalize_value(diff['children'])
    key = diff['key']
    lines.append(
        f'{indent}{key}: {make_diff(children, depth=depth + 1)}'
    )


def get_status(diff):
    if 'status' in diff:
        return diff['status']


def normalize_value(value):
    if value in (False, True):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, dict):
        for v in value.values():
            v = normalize_value(v)
    return value
