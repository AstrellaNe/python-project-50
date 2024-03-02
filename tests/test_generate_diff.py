# Импортируем необходимые модули
import json
import tempfile
from gendiff.gendiff import generate_diff  # Импортируем функцию

def test_no_file():
    """Проверка поведения функции при отсутствии файла."""
    # Пути к несуществующим файлам
    path_to_nonexistent_file1 = 'nonexistent_file1.json'
    path_to_nonexistent_file2 = 'nonexistent_file2.json'
    # Проверяем, что функция возвращает None, если файлы не существуют
    assert generate_diff(path_to_nonexistent_file1, path_to_nonexistent_file2) is None
    
def test_generate_diff():
    """Проверка работы функции на различных файлах."""
    # Создаем временные файлы с тестовыми данными
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.json') as temp1, tempfile.NamedTemporaryFile('w', delete=False, suffix='.json') as temp2:
        # Записываем тестовые данные во временные файлы
        json.dump({"name": "John", "age": 30}, temp1)
        json.dump({"name": "Alice", "age": 25}, temp2)
        temp1.flush()  # Убеждаемся, что данные записаны
        temp2.flush()
        
        # Сравниваем содержимое файлов с помощью функции
        # Предполагаем, что функция выведет изменения в формате:
        expected_output = """{
- age: 30
+ age: 25
- name: John
+ name: Alice
}"""
        assert generate_diff(temp1.name, temp2.name) == expected_output


def test_identical_files():
    """Тестирование с двумя идентичными файлами."""
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.json') as temp:
        json.dump({"key": "value"}, temp)
        temp.flush()
        assert generate_diff(temp.name, temp.name) == '{\n  key: value\n}'


def test_added_data():
    """Тестирование при добавлении данных во второй файл."""
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.json') as temp1, tempfile.NamedTemporaryFile('w', delete=False, suffix='.json') as temp2:
        json.dump({"key": "value"}, temp1)
        json.dump({"key": "value", "new_key": "new_value"}, temp2)
        temp1.flush()
        temp2.flush()
        expected_output = "{\n  key: value\n+ new_key: new_value\n}"
        assert generate_diff(temp1.name, temp2.name) == expected_output


def test_removed_data():
    """Тестирование при удалении данных из второго файла."""
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.json') as temp1, tempfile.NamedTemporaryFile('w', delete=False, suffix='.json') as temp2:
        json.dump({"key": "value", "to_remove": "gone"}, temp1)
        json.dump({"key": "value"}, temp2)
        temp1.flush()
        temp2.flush()
        expected_output = "{\n  key: value\n- to_remove: gone\n}"
        assert generate_diff(temp1.name, temp2.name) == expected_output


def test_different_types():
    """Тестирование при изменении типов данных между файлами."""
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.json') as temp1, tempfile.NamedTemporaryFile('w', delete=False, suffix='.json') as temp2:
        json.dump({"key": "value", "to_change": "string"}, temp1)
        json.dump({"key": "value", "to_change": ["list"]}, temp2)
        temp1.flush()
        temp2.flush()
        expected_output = "{\n  key: value\n- to_change: string\n+ to_change: ['list']\n}"
        assert generate_diff(temp1.name, temp2.name) == expected_output
