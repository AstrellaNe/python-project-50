import pytest
from gendiff.scripts.gendiff import generate_diff


# Параметризованные тесты (все скопом)
@pytest.mark.parametrize(
    "formatter, test_case, file1, file2, expected_dir, expected_file_suffix",
    [
        ('json', 'added', 'original_data.json', 'changed_data.json',
         'json', 'expected_diff_added_data.txt'),
        ('json', 'removed', 'original_data.json', 'reduced_data.json',
         'json', 'expected_diff_removed_data.txt'),
        ('json', 'nested', 'nested_original.json', 'nested_changed.json',
         'json', 'expected_diff_nested.txt'),
        ('json', 'empty', 'original_data.json', 'original_data.json',
         'json', 'expected_diff_identical_files.txt'),
        ('json', 'similar', 'original_data.json', 'original_data.json',
         'json', 'expected_diff_identical_files.txt'),
        ('plain', 'added', 'original_data.json', 'changed_data.json',
         'plain', 'expected_diff_added_data.txt'),
        ('plain', 'removed', 'original_data.json', 'reduced_data.json',
         'plain', 'expected_diff_removed_data.txt'),
        ('plain', 'nested', 'nested_original.json', 'nested_changed.json',
         'plain', 'expected_diff_nested.txt'),
        ('plain', 'empty', 'original_data.json', 'original_data.json',
         'plain', 'expected_diff_identical_files.txt'),
        ('plain', 'similar', 'original_data.json', 'original_data.json',
         'plain', 'expected_diff_identical_files.txt'),
        ('stylish', 'added', 'original_data.json', 'changed_data.json',
         'stylish', 'expected_diff_added_data.txt'),
        ('stylish', 'removed', 'original_data.json', 'reduced_data.json',
         'stylish', 'expected_diff_removed_data.txt'),
        ('stylish', 'nested', 'nested_original.json', 'nested_changed.json',
         'stylish', 'expected_diff_nested.txt'),
        ('stylish', 'empty', 'original_data.json', 'original_data.json',
         'stylish', 'expected_diff_identical_files.txt'),
        ('stylish', 'similar', 'original_data.json', 'original_data.json',
         'stylish', 'expected_diff_identical_files.txt'),
    ]
)
def test_generate_diff(
        formatter, test_case, file1, file2, expected_dir, expected_file_suffix):
    # Определение путей к файлам данных
    file1_path = f'tests/fixtures/{file1}'
    file2_path = f'tests/fixtures/{file2}'
    expected_path = f'tests/fixtures/{expected_dir}/{expected_file_suffix}'

    # Генерация результата
    result = generate_diff(file1_path, file2_path, formatter)

    # Чтение ожидаемого результата
    with open(expected_path) as ef:
        expected = ef.read().strip()

    # Проверка результата
    assert result.strip() == expected
