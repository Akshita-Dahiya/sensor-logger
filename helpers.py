import csv

def load_column(filename, column):
    values = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            values.append(float(row[column]))
    return values