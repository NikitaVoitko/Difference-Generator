import os
from gendiff.engine import generate_diff


def test_generate_diff_json():
    path1 = os.path.join(os.path.dirname(__file__), 'fixtures/input_files/',
                         'file1.yml')
    path2 = os.path.join(os.path.dirname(__file__), 'fixtures/input_files/',
                         'file2.yml')

    expected_path = os.path.join(os.path.dirname(__file__),
                                 'fixtures/result_files/json/',
                                 'result_yml_flat.txt')
    with open(expected_path, 'r') as file:
        expected = file.read()

    assert generate_diff(path1, path2, 'json') == expected
