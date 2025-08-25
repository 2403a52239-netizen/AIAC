def validate_indian_mobile():
    number = input("Enter an Indian mobile number: ").strip()
    if len(number) == 10 and number.isdigit() and number[0] in '6789':
        print("Valid Indian mobile number.")
    else:
        print("Invalid Indian mobile number.")

validate_indian_mobile()
