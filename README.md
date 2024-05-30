
### Hexlet tests and linter status:
[![Actions Status](https://github.com/AstrellaNe/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AstrellaNe/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a8b02b8e203dc4a94661/maintainability)](https://codeclimate.com/github/AstrellaNe/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a8b02b8e203dc4a94661/test_coverage)](https://codeclimate.com/github/AstrellaNe/python-project-50/test_coverage)

## Описание проекта

Этот проект предназначен для сравнения конфигурационных файлов различных форматов (JSON, YAML) и вывода различий в нескольких форматах (plain, stylish, json).

## Установка

Примечание: для проект тестировался на версяих Python не ниже 3.10. Рекомендуется установка Python 3.12. Работоспособность на версиях ниже не гарантируется.
Примечание: для работы с проекто требуется версия Poetry не ниже version 1.2.2

```bash
git clone https://github.com/AstrellaNe/python-project-50.git
cd python-project-50
make install
```

## Использование

### Сравнение двух файлов с выводом различий в формате Stylish (по умолчанию)

```bash
gendiff path/to/file1 path/to/file2
```

### Сравнение двух файлов с выводом различий в формате Plain

```bash
gendiff --format plain path/to/file1 path/to/file2
```

### Сравнение двух файлов с выводом различий в формате JSON

```bash
gendiff --format json path/to/file1 path/to/file2
```

### Вызов помощи

```bash
gendiff --help
```

## Видео с примерами работы пакета

**Пример работы форматтера JSON**
[![asciicast](https://asciinema.org/a/XuSt15fRljYBIwN1IGrcT2Knn.svg)](https://asciinema.org/a/XuSt15fRljYBIwN1IGrcT2Knn)

**Пример работы форматтеров Plain и Stylish**
[![asciicast](https://asciinema.org/a/vE6SCX1Zk25hjAXImyS3TckB9.svg)](https://asciinema.org/a/vE6SCX1Zk25hjAXImyS3TckB9)

**Простое сравнение двух файлов в формате JSON и вызов помощи**
[![asciicast](https://asciinema.org/a/DfCMzLrpG3Gc2JdQ4WinhhCPD.svg)](https://asciinema.org/a/DfCMzLrpG3Gc2JdQ4WinhhCPD)

**Сравнение двух плоских файлов формата YAML, случай файл не найден (+ формат JSON)**
[![asciicast](https://asciinema.org/a/cIO7yVg654FZzgUvCy3xPdyfp.svg)](https://asciinema.org/a/cIO7yVg654FZzgUvCy3xPdyfp)

## Модули проекта

- **arg_parser**: модуль, ответственный за парсинг аргументов командной строки.
- **differ**: основной модуль для генерации различий между файлами.
- **formatters**: форматтеры
  - **json**: форматтер для вывода различий в формате JSON.
  - **plain**: форматтер для вывода различий в плоском стиле.
  - **stylish**: форматтер для вывода красивого дерева различий.
- **loader**: модуль, ответственный за загрузку и возврат данных из файлов.
- **gendiff**: основной модуль, связывающий все компоненты и обеспечивающий выполнение программы.

## Использование форматтеров

Для использования форматтеров используйте флаг \`--format\` или \`-f\`, за которым следует один из доступных форматов \`stylish\`, \`plain\` или \`json\`. Если флаг \`--format\` не указан, по умолчанию применяется формат \`stylish\`.

Примеры использования:

```bash
gendiff --format plain path/to/file1 path/to/file2
gendiff --f json path/to/file1 path/to/file2
```