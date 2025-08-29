import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        groups = match.groups()
        for group in groups:
            number = int(group)
            if number < 0 or number > 255:
                return False

        return True
    else:
        return False


if __name__ == "__main__":
    main()
