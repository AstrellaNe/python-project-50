import pytest
from gendiff.scripts.gendiff import generate_diff

def test_no_file():
    """Проверка поведения функции при отсутствии файла."""
    path_to_nonexistent_file1 = 'nonexistent_file1.json'
    path_to_nonexistent_file2 = 'nonexistent_file2.json'
    assert generate_diff(path_to_nonexistent_file1, path_to_nonexistent_file2) is None

@pytest.mark.parametrize("original_file, changed_file, expected_file", [
    ("original_data.json", "changed_data.json", "expected_diff_original_changed.txt"),
    ("original_data.yaml", "changed_data.yml", "expected_diff_original_changed.txt"),  # YAML files
])
def test_generate_diff(original_file, changed_file, expected_file, fixtures_dir):
    """Проверка работы функции на различных файлах."""
    with open(f'{fixtures_dir}/{expected_file}', 'r') as file:
        expected_diff = file.read()
    assert generate_diff(f'{fixtures_dir}/{original_file}', f'{fixtures_dir}/{changed_file}') == expected_diff

@pytest.mark.parametrize("original_file, expected_file", [
    ("original_data.json", "expected_diff_identical_files.txt"),
    ("original_data.yaml", "expected_diff_identical_files.txt"),  # YAML file
])
def test_identical_files(original_file, expected_file, fixtures_dir):
    """Тестирование двух идентичных файлов."""
    with open(f'{fixtures_dir}/{expected_file}', 'r') as file:
        expected_diff = file.read()
    assert generate_diff(f'{fixtures_dir}/{original_file}', f'{fixtures_dir}/{original_file}') == expected_diff

@pytest.mark.parametrize("original_file, changed_file, expected_file", [
    ("original_data.json", "changed_data.json", "expected_diff_added_data.txt"),
    ("original_data.yaml", "changed_data.yml", "expected_diff_added_data.txt"),  # YAML files
])
def test_added_data(original_file, changed_file, expected_file, fixtures_dir):
    """Тестирование при добавлении данных во второй файл."""
    with open(f'{fixtures_dir}/{expected_file}', 'r') as file:
        expected_diff = file.read()
    assert generate_diff(f'{fixtures_dir}/{original_file}', f'{fixtures_dir}/{changed_file}') == expected_diff

@pytest.mark.parametrize("original_file, reduced_file, expected_file", [
    ("original_data.json", "reduced_data.json", "expected_diff_removed_data.txt"),
    ("original_data.yaml", "reduced_data.yaml", "expected_diff_removed_data.txt"),  # YAML files
])
def test_removed_data(original_file, reduced_file, expected_file, fixtures_dir):
    """Тестирование при удалении данных из второго файла."""
    with open(f'{fixtures_dir}/{expected_file}', 'r') as file:
        expected_diff = file.read()
    assert generate_diff(f'{fixtures_dir}/{original_file}', f'{fixtures_dir}/{reduced_file}') == expected_diff

@pytest.mark.parametrize("original_file, changed_file, expected_file", [
    ("original_data.json", "different_types_data.json", "expected_diff_different_types.txt"),
    ("original_data.yaml", "different_types_data.yaml", "expected_diff_different_types.txt"),  # YAML files
])
def test_different_types(original_file, changed_file, expected_file, fixtures_dir):
    """Тестирование при изменении типов данных между файлами."""
    with open(f'{fixtures_dir}/{expected_file}', 'r') as file:
        expected_diff = file.read()
    assert generate_diff(f'{fixtures_dir}/{original_file}', f'{fixtures_dir}/{changed_file}') == expected_diff
