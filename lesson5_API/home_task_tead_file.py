import json
from csv import DictReader

# Чтение файлов
with open("../folder/users.json", "r") as json_file:
    users = json.loads(json_file.read())

with open("../folder/books.csv", newline="") as csv_file:
    reader = DictReader(csv_file)
    rows = list(reader)

# Запись в result.json
with open("result.json", "w") as file:
    s = json.dumps(users, indent=4)
    v = json.dumps(rows, indent=4)
    file.write(s + v)
