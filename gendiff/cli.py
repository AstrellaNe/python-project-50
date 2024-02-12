from gendiff.scripts.gendiff import generate_diff


def main():
    file1 = input("Enter the path to the first JSON file: ")
    file2 = input("Enter the path to the second JSON file: ")
    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == '__main__':
    main()
