import os
import pytest
from gendiff.scripts.gendiff import generate_diff


# Вспомогательная функция для загрузки ожидаемого вывода
def load_expected_output(fixtures_dir, filename):
    file_path = os.path.join(fixtures_dir, 'stylish_exp', filename)
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.mark.parametrize("original_file, changed_file, expected_file", [
    ("original_data.json", "changed_data.json", "expected_diff_original_changed.txt"),
    ("original_data.yaml", "changed_data.yml", "expected_diff_original_changed.txt"),
])
def test_generate_diff(original_file, changed_file, expected_file, fixtures_dir):
    """Тестирует диффер между двумя файлами."""
    expected_diff = load_expected_output(fixtures_dir, expected_file)
    diff = generate_diff(os.path.join(fixtures_dir, original_file), os.path.join(fixtures_dir, changed_file), format_name='stylish')
    assert diff == expected_diff


def test_no_file():
    """Тест при попытке обработки несуществующих файлов. Проверяет, что функция возвращает None."""
    path_to_nonexistent_file1 = 'nonexistent_file1.json'
    path_to_nonexistent_file2 = 'nonexistent_file2.json'
    result = generate_diff(path_to_nonexistent_file1, path_to_nonexistent_file2, format_name='stylish')
    assert result is None, "Ожидалось, что функция вернёт None для несуществующих файлов"


@pytest.mark.parametrize("original_file, expected_file", [
    ("original_data.json", "expected_diff_identical_files.txt"),
    ("original_data.yaml", "expected_diff_identical_files.txt"),  # YAML file
])
def test_identical_files(original_file, expected_file, fixtures_dir):
    """Тестирует случай с двумя идентичными файлами."""
    expected_diff = load_expected_output(fixtures_dir, expected_file)
    actual_diff = generate_diff(os.path.join(fixtures_dir, original_file), os.path.join(fixtures_dir, original_file), format_name='stylish')
    assert actual_diff == expected_diff


@pytest.mark.parametrize("original_file, changed_file, expected_file", [
    ("original_data.json", "changed_data.json", "expected_diff_added_data.txt"),
    ("original_data.yaml", "changed_data.yml", "expected_diff_added_data.txt"),  # YAML files
])
def test_added_data(original_file, changed_file, expected_file, fixtures_dir):
    """Тестирует добавление данных во второй файл."""
    expected_diff = load_expected_output(fixtures_dir, expected_file)
    actual_diff = generate_diff(os.path.join(fixtures_dir, original_file), os.path.join(fixtures_dir, changed_file), format_name='stylish')
    assert actual_diff == expected_diff


@pytest.mark.parametrize("original_file, reduced_file, expected_file", [
    ("original_data.json", "reduced_data.json", "expected_diff_removed_data.txt"),
    ("original_data.yaml", "reduced_data.yaml", "expected_diff_removed_data.txt"),  # YAML files
])
def test_removed_data(original_file, reduced_file, expected_file, fixtures_dir):
    """Тестирует удаление данных из второго файла."""
    expected_diff = load_expected_output(fixtures_dir, expected_file)
    actual_diff = generate_diff(os.path.join(fixtures_dir, original_file), os.path.join(fixtures_dir, reduced_file), format_name='stylish')
    assert actual_diff == expected_diff


@pytest.mark.parametrize("original_file, changed_file, expected_file", [
    ("original_data.json", "different_types_data.json", "expected_diff_different_types.txt"),
    ("original_data.yaml", "different_types_data.yaml", "expected_diff_different_types.txt"),  # YAML files
])
def test_different_types(original_file, changed_file, expected_file, fixtures_dir):
    """Тестирует изменение типов данных между файлами."""
    expected_diff = load_expected_output(fixtures_dir, expected_file)
    actual_diff = generate_diff(os.path.join(fixtures_dir, original_file), os.path.join(fixtures_dir, changed_file), format_name='stylish')
    assert actual_diff == expected_diff


@pytest.mark.parametrize("original_file, changed_file, expected_file", [
    ("nested_original.json", "nested_changed.json", "expected_diff_nested.txt"),
    ("nested_original.yaml", "nested_changed.yaml", "expected_diff_nested.txt"),  # YAML files
])
def test_nested_simple(original_file, changed_file, expected_file, fixtures_dir):
    """Тестирует вложенность структур, как в оригинальном примере задания."""
    expected_diff = load_expected_output(fixtures_dir, expected_file)
    actual_diff = generate_diff(os.path.join(fixtures_dir, original_file), os.path.join(fixtures_dir, changed_file), format_name='stylish')
    assert actual_diff == expected_diff
