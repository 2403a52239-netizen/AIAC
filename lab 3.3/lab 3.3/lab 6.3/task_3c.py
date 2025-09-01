def classify_age_group(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

age = int(input("Enter age: "))
group = classify_age_group(age)
print(f"Age group: {group}")
