from old_ver.generate_diff import generate_diff

def test_no_file():
    """Проверка поведения функции при отсутствии файла."""
    path_to_nonexistent_file1 = 'nonexistent_file1.json'
    path_to_nonexistent_file2 = 'nonexistent_file2.json'
    expected_output = '{\n\n}'  # ожидаемый вывод
    assert generate_diff(path_to_nonexistent_file1, 
                         path_to_nonexistent_file2) == expected_output
    
    
def test_generate_diff():
    arr1 = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    arr2 = [{"name": "Alice", "age": 25}, {"name": "John", "age": 30}]
    
    # Тест на эквивалентность массивов
    assert generate_diff(arr1, arr2) == True
    
    # Тест на неэквивалентность массивов при разных данных
    arr3 = [{"name": "John", "age": 31}]  # Измененный возраст
    assert generate_diff(arr1, arr3) == False
    
    # Тест на неэквивалентность при разном количестве элементов
    arr4 = [{"name": "Alice", "age": 25}]
    assert generate_diff(arr1, arr4) == False
