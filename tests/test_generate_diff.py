# Импортируем необходимые модули
from gendiff.gendiff import generate_diff  # Импортируем функцию


def test_no_file():
    """Проверка поведения функции при отсутствии файла."""
    # Пути к несуществующим файлам
    path_to_nonexistent_file1 = 'nonexistent_file1.json'
    path_to_nonexistent_file2 = 'nonexistent_file2.json'
    # Проверяем, что функция возвращает None, если файлы не существуют
    assert generate_diff(path_to_nonexistent_file1, path_to_nonexistent_file2) is None


def test_generate_diff(original_file, changed_file):
    """Проверка работы функции на различных файлах."""
    expected_output = """{
  key: value
- to_change: string
+ to_change: ['list']
- to_remove: gone
}"""
    assert generate_diff(original_file, changed_file) == expected_output


def test_identical_files(original_file):
    """Тестирование с двумя идентичными файлами."""
    expected_output = """{
  key: value
  to_change: string
  to_remove: gone
}"""
    assert generate_diff(original_file, original_file) == expected_output


def test_added_data(original_file, changed_file):
    """Тестирование при добавлении данных во второй файл."""
    expected_output = """{
  key: value
- to_change: string
+ to_change: ['list']
- to_remove: gone
}"""
    assert generate_diff(original_file, changed_file) == expected_output


def test_removed_data(original_file, reduced_file):
    """Тестирование при удалении данных из второго файла."""
    expected_output = """{
  key: value
- to_change: string
- to_remove: gone
}"""
    assert generate_diff(original_file, reduced_file) == expected_output


def test_different_types(original_file, changed_file):
    """Тестирование при изменении типов данных между файлами."""
    expected_output = """{
  key: value
- to_change: string
+ to_change: ['list']
- to_remove: gone
}"""
    assert generate_diff(original_file, changed_file) == expected_output
