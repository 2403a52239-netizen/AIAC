def classify_age_group(age):
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        group = classify_age_group(age)
        print(f"You are classified as: {group}")
    except ValueError:
        print("Please enter a valid integer for age.")