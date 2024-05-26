import os
import pytest
from gendiff.diff import generate_diff


@pytest.mark.parametrize("file1, file2, result_file, format", [
    ('file1.json', 'file2.json', 'result_json_nested.txt', None),
    ('file1.json', 'file2.json', 'result_json_nested.txt', 'plain'),
    ('file1.yml', 'file2.yml', 'result_yml_nested.txt', 'json'),
    ('file1.yml', 'file2.yml', 'result_yml_nested.txt', 'plain'),
    ('file1.yml', 'file2.yml', 'result_yml_nested.txt', None),
])
def test_generate_diff(file1, file2, result_file, format):
    path1 = os.path.join(os.path.dirname(__file__), 'fixtures/input_files/',
                         file1)
    path2 = os.path.join(os.path.dirname(__file__), 'fixtures/input_files/',
                         file2)
    result_path = 'stylish' if format is None else format
    expected_path = os.path.join(
        os.path.dirname(__file__),
        f'fixtures/result_files/{result_path}/',
        result_file
    )

    with open(expected_path, 'r') as file:
        expected = file.read()

    if format:
        assert generate_diff(path1, path2, format) == expected
    else:
        assert generate_diff(path1, path2) == expected
