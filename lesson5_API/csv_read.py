import csv
from csv import DictReader

with open('../lesson5_API/csv.csv', "r") as file:
    print(file.read())
    reader = csv.reader(file)

#     # Извлекаем заголовок
#     header = next(reader)
#
#     # Интегрируемся по данным делаем из них словори
#     for row in reader:
#         print(dict(zip(header, row)))
#
# print(100 * "+")
#
# with open('../lesson5_API/csv.csv', newline="") as file:
#     reader = DictReader(file)
#
#     # Интегрируемся по данным делая из ниъ словари
#     for row in reader:
#         print(row)
