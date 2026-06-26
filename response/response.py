from validator_collection import validators, checkers, errors

email_input = input("What's your email address? ")


if email_address := validators.email(email_input):
    print("Valid")
else:
    print("Invalid")

