# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as inp_file:  # TODO считать содержимое csv файла
        reader = csv.DictReader(inp_file)
        rows = [row for row in reader]
    with open(OUTPUT_FILENAME, "w") as out_file:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(rows, out_file, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
