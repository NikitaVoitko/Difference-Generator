from gendiff.parser import load_file
from gendiff.tree import build_diff
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file_content1 = load_file(file_path1)
    file_content2 = load_file(file_path2)

    diff = build_diff(file_content1, file_content2)
    format_diff = make_format(diff, formatter)

    return format_diff


def make_format(data, formatter):
    if formatter == 'plain':
        return get_plain(data)
    elif formatter == 'json':
        return get_json(data)
    elif formatter == 'stylish':
        return get_stylish(data)
    else:
        raise Exception('Wrong format')
