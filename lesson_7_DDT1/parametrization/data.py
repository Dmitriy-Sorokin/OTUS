import csv

def get_auth_endpoint():
    with open("csv.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for el in reader:
            yield el

auth_endpoint = get_auth_endpoint()
