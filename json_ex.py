import json
import string
import random


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


a = random.randint(1, 9999)
b = random.randint(1, 99)
json_data = {
    "id": a,
    "name": f"{random_char(10)}",
    "age": b,
    "secretIdentity": f"{random_char(35)}",
    "powers": [
        f"{random_char(10)}",
        f"{random_char(9)}",
        f"{random_char(8)}"
    ]
}

for i in range(50):
    # 1. Read file contents
    with open("data_file.json", "r") as file:
        data = json.load(file)
    data.append(json_data)
    with open("data_file.json", "w") as file:
        json.dump(data, file, indent=4)
