import os
from gendiff.gendiff import generate_diff


def main():
    file_path1 = input("Enter the path to the first JSON file: ")
    file_path2 = input("Enter the path to the second JSON file: ")
    
    # Получаем абсолютные пути к файлам
    file1 = os.path.abspath(file_path1)
    file2 = os.path.abspath(file_path2)

    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == '__main__':
    main()
