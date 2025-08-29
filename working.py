import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    matches = re.search(pattern, s)

    if not matches:
        raise ValueError

    g1 = matches.group(1)
    g1 = int(g1)
    g2 = matches.group(2)
    g3 = matches.group(3)
    g4 = matches.group(4)
    g4 = int(g4)
    g5 = matches.group(5)
    g6 = matches.group(6)
    
    if (g2 and int(g2) >= 60) or (g5 and int(g5) >= 60):
        raise ValueError
    if g2:
        g2 = int(g2)
    else:
        g2 = 0
    if g5:
        g5 = int(g5)
    else:
        g5 = 0

    def to_24_hour(hour, minute, period):
            if period == "AM":
                if hour == 12:
                    hour = 0
            else:
                if hour != 12:
                    hour += 12
            return f"{hour:02}:{minute:02}"

    first_time = to_24_hour(g1, g2, g3)
    last_time = to_24_hour(g4, g5, g6)

    return f"{first_time} to {last_time}"

if __name__ == "__main__":
    main()
