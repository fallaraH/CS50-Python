import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    nlines = 0
    FILENAME = sys.argv[1]

    with open(FILENAME) as file:
        for line in file:
            line = line.lstrip()
            if line.startswith("#") or line == "":
                continue
            else:
                nlines += 1

    print(nlines)

except FileNotFoundError:
    print("File does not exist")

