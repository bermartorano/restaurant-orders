import csv


def csv_data(file_path: str):
    with open(file_path) as file:
        csv_file = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = csv_file
    return data
