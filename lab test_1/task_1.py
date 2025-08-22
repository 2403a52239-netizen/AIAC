
def classify_age_group(age):
    """
    Classifies a person into an age group based on their age.

    Parameters:
        age (int): The age of the person.

    Returns:
        str: The age group ('Child', 'Teenager', 'Adult', 'Senior').
    """
    # Check for invalid (negative) age
    if age < 0:
        return "Invalid age"
    # Ages 0 to 12 are classified as 'Child'
    elif age <= 12:
        return "Child"
    # Ages 13 to 17 are classified as 'Teenager'
    elif age <= 17:
        return "Teenager"
    # Ages 18 to 60 are classified as 'Adult'
    elif age <= 60:
        return "Adult"
    # Ages above 60 are classified as 'Senior'
    else:
        return "Senior"

# Get user input
try:
    user_input = int(input("Enter your age: "))
    age_group = classify_age_group(user_input)
    print(f"You belong to the '{age_group}' age group.")
except ValueError:
    print("Please enter a valid integer for age.")