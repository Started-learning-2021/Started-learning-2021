import csv
from typing import List, Sequence

'''
Returns a list of rows and it's field names read from a CSV file
'''
def readCSV(filepath: str, delimiter=','):
    rows = []

    with open(filepath) as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        for row in reader:
            rows.append(row)

    return rows, rows[0]

'''
Writes a list of rows to a CSV file
'''
def writeCSV(rows: List, fieldnames: Sequence, filepath: str, delimiter=','):
    with open(filepath, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=delimiter)

        writer.writerows(rows)
