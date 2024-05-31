import json
import yaml


def parse_content(content, extension):
    """
    Парсит содержимое файла в зависимости от расширения.

    Args:
        content (str): Содержимое файла в виде строки.
        extension (str): Расширение файла.

    Returns:
        dict: Словарь с данными из файла.

    Raises:
        ValueError: Если формат файла не поддерживается.
    """
    if extension == '.json':
        return json.loads(content)
    if extension in ('.yaml', '.yml'):
        return yaml.safe_load(content)
    raise ValueError(f'Unsupported file format: {extension}')


def read_file(filepath):
    """
    Читает файл и возвращает его содержимое в виде словаря.

    Args:
        filepath (str): Путь к файлу.

    Returns:
        dict: Словарь с данными из файла.
    """
    with open(filepath) as file:
        content = file.read()
        extension = filepath.split('.')[-1]
        extension = f".{extension}"
        return parse_content(content, extension)
