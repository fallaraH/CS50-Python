import sys
import csv

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    students = []
    FILENAME = sys.argv[1]
    NEWFILENAME = sys.argv[2]

    with open(FILENAME) as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            last, first = name.split(", ")
            student = {"first": first, "last": last, "house": row["house"]}
            students.append(student)

    with open(NEWFILENAME, "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
