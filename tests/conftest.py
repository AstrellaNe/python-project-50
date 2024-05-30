import pytest
import os


# Фикстура для получения пути к директории с фикстурами
@pytest.fixture
def fixtures_dir():
    # Возвращаем абсолютный путь к директории с фикстурами
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')


# Фикстура для получения пути к файлу с исходными данными
@pytest.fixture
def original_file(fixtures_dir):
    # Соединяем путь к директории с именем файла
    return os.path.join(fixtures_dir, 'original_data.json')


# Фикстура для получения пути к измененному файлу данных
@pytest.fixture
def changed_file(fixtures_dir):
    # Соединяем путь к директории с именем файла
    return os.path.join(fixtures_dir, 'changed_data.json')


# Фикстура для получения пути к уменьшенному файлу данных
@pytest.fixture
def reduced_file(fixtures_dir):
    # Соединяем путь к директории с именем файла
    return os.path.join(fixtures_dir, 'reduced_data.json')


# Фикстуры для чтения ожидаемых результатов из текстовых файлов
@pytest.fixture
def expected_diff_original_changed(fixtures_dir):
    # Чтение файла с ожидаемыми результатами
    with open(os.path.join(fixtures_dir,
                           'expected_diff_original_changed.txt'), 'r') as file:
        return file.read()


@pytest.fixture
def expected_diff_identical_files(fixtures_dir):
    # Чтение файла с ожидаемыми результатами
    with open(os.path.join(fixtures_dir,
                           'expected_diff_identical_files.txt'), 'r') as file:
        return file.read()


@pytest.fixture
def expected_diff_added_data(fixtures_dir):
    # Чтение файла с ожидаемыми результатами
    with open(os.path.join(fixtures_dir,
                           'expected_diff_added_data.txt'), 'r') as file:
        return file.read()


@pytest.fixture
def expected_diff_removed_data(fixtures_dir):
    # Чтение файла с ожидаемыми результатами
    with open(os.path.join(fixtures_dir,
                           'expected_diff_removed_data.txt'), 'r') as file:
        return file.read()


@pytest.fixture
def expected_diff_different_types(fixtures_dir):
    # Чтение файла с ожидаемыми результатами
    with open(os.path.join(fixtures_dir,
                           'expected_diff_different_types.txt'), 'r') as file:
        return file.read()
