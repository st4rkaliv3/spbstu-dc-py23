import json
FILENAME = "input.json"


def task() -> float:
    with (open(FILENAME, "r") as f):
        data = json.load(f)
        sum_of_prods = round(sum([line['score'] * line['weight'] for line in data]), 3)
        return sum_of_prods


print(task())
