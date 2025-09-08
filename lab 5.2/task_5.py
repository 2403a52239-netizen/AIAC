def greet_user(name, gender):
    gender = gender.lower()
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Mrs."
    else:
        title = "Mx."
    return f"Hello, {title} {name}! Welcome."

if __name__ == "__main__":
    name = input("Enter your name: ")
    gender = input("Enter your gender (male/female/other): ")
    print(greet_user(name, gender))