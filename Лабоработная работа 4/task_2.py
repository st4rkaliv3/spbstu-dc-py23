import csv
import json


INPUT_FILENAME = "input.csv"
INPUT_DELIMITER = ","
INPUT_LINE_TERMINATOR = "\n"
OUTPUT_FILENAME = "output.json"
OUTPUT_INDENT = 4


def task() -> None:
    with (open(INPUT_FILENAME, "r") as csv_file):
        reader = csv.DictReader(csv_file, delimiter=INPUT_DELIMITER, lineterminator=INPUT_LINE_TERMINATOR)
        data = [row for row in reader]
        with (open(OUTPUT_FILENAME, "w") as json_file):
            json.dump(data, json_file, indent=OUTPUT_INDENT, ensure_ascii=True)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
