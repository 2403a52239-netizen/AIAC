#refactor the code using elif statements

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print(grade(85))  # Output: B
#test cases
print(grade(95))  # Output: A
print(grade(75))  # Output: C
print(grade(65))  # Output: D
