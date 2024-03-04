from gendiff.scripts.gendiff import generate_diff


def test_no_file():
    """Проверка поведения функции при отсутствии файла."""
    path_to_nonexistent_file1 = 'nonexistent_file1.json'
    path_to_nonexistent_file2 = 'nonexistent_file2.json'
    assert generate_diff(path_to_nonexistent_file1, path_to_nonexistent_file2) is None


def test_generate_diff(original_file, changed_file, expected_diff_original_changed):
    """Проверка работы функции на различных файлах."""
    assert generate_diff(original_file, changed_file) == expected_diff_original_changed


def test_identical_files(original_file, expected_diff_identical_files):
    """Тестирование двух идентичных файлов."""
    assert generate_diff(original_file, original_file) == expected_diff_identical_files


def test_added_data(original_file, changed_file, expected_diff_added_data):
    """Тестирование при добавлении данных во второй файл."""
    assert generate_diff(original_file, changed_file) == expected_diff_added_data


def test_removed_data(original_file, reduced_file, expected_diff_removed_data):
    """Тестирование при удалении данных из второго файла."""
    assert generate_diff(original_file, reduced_file) == expected_diff_removed_data


def test_different_types(original_file, changed_file, expected_diff_different_types):
    """Тестирование при изменении типов данных между файлами."""
    assert generate_diff(original_file, changed_file) == expected_diff_different_types
