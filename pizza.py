import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    table = []
    FILENAME = sys.argv[1]

    with open(FILENAME) as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            table.append(row)


    print(tabulate(table, headers, tablefmt="grid"))
    
except FileNotFoundError:
    sys.exit("File does not exist")
