from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birth_date_str = input("Date of Birth: ")
    minutes = minutes_since_birth(birth_date_str)
    print(f"{minutes} minutes")

def minutes_since_birth(birth_date_str):
    try:
        birth_date = date.fromisoformat(birth_date_str)
    except ValueError:
        sys.exit("Invalid Date")

    todays_date = date.today()
    delta = todays_date - birth_date
    total_minutes = round(delta.days * 24 * 60)
    return p.number_to_words(total_minutes, andword="").capitalize()

if __name__ == "__main__":
    main()

