# Импортируем необходимые модули
import json
import tempfile
from gendiff.scripts.gendiff import generate_diff  # Импортируем функцию

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
