import re

def main():
    print(count(input("Text: ")))


def count(s:str) -> int:
    searcher = re.findall(r"\bum\b[^\w]?", s, re.IGNORECASE)
    searcher = int(len(searcher))

    return searcher



if __name__ == "__main__":
    main()
