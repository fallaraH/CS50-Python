import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^.+src=\"https?://(?:www\.)?youtube\.com/embed/(.+?)\".+$", s)
    if matches:
        shorten = "https://youtu.be/" + matches.group(1)
        return shorten


if __name__ == "__main__":
    main()
