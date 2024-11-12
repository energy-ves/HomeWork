# TODO решите задачу
import json

input_file_name = "input.json"


def task() -> float:
    with open(input_file_name) as file:
        json_data = json.load(file) # десериализация данных
    return sum([dict_["score"] * dict_["weight"] for dict_ in json_data ]) # возвращение суммы произведений двух значений всех словарей


print(f"{task():.3f}")

