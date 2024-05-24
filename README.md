### Hexlet tests and linter status:
[![Actions Status](https://github.com/AstrellaNe/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AstrellaNe/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a8b02b8e203dc4a94661/maintainability)](https://codeclimate.com/github/AstrellaNe/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a8b02b8e203dc4a94661/test_coverage)](https://codeclimate.com/github/AstrellaNe/python-project-50/test_coverage)


## Видео с примерами работы пакета

**Пример работы форматтеров Plain и Stylish**
[![asciicast](https://asciinema.org/a/vE6SCX1Zk25hjAXImyS3TckB9.svg)](https://asciinema.org/a/vE6SCX1Zk25hjAXImyS3TckB9)

**Простое сравнение двух файлов формат JSON и вызов помощи**
[![asciicast](https://asciinema.org/a/DfCMzLrpG3Gc2JdQ4WinhhCPD.svg)](https://asciinema.org/a/DfCMzLrpG3Gc2JdQ4WinhhCPD)

**Cравнение двух плоских файлов формата YAML, случай файл не найден (+ формат JSON)**
[![asciicast](https://asciinema.org/a/cIO7yVg654FZzgUvCy3xPdyfp.svg)](https://asciinema.org/a/cIO7yVg654FZzgUvCy3xPdyfp)


Пока инструкция на будущее без форматирования
loader - модуль, ответственный за загрузку и возврат данных из файлов
stylish - форматтер для вывода красивого дерева различий
plain - форматтер для вывода плоского стиля

Использование форматтеров:
gendiff --format или -f (далее выбор stylish или plain) [пути до файлов]
Если использовать без флага --format / -f , то по умолчанию применяется stylish