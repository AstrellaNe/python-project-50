import pytest
import os

# Фикстура для пути к тестовым файлам
@pytest.fixture
def test_files_dir():
    # Получаем абсолютный путь к директории, где находится файл conftest.py
    return os.path.dirname(os.path.abspath(__file__))

# Фикстуры для путей к конкретным тестовым файлам
@pytest.fixture
def original_file(test_files_dir):
    return os.path.join(test_files_dir, 'original_data.json')

@pytest.fixture
def changed_file(test_files_dir):
    return os.path.join(test_files_dir, 'changed_data.json')

@pytest.fixture
def reduced_file(test_files_dir):
    return os.path.join(test_files_dir, 'reduced_data.json')
