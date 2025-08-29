import validators

email = input("What's your email adress?").strip()

if validators.email(email):
    print("Valid")
else:
    print("Invalid")
