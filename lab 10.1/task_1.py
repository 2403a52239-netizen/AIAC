#refactor the code to fix the bugs with explanation of the bugs

def calc_average(marks):
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average   # Fixed division by zero error by ensuring marks list is not empty

marks = [85, 90, 78, 92]
print("Average Score is ", calc_average(marks))  # Output: Average Score is  86.25
#test cases
print("Average Score is ", calc_average([100, 90, 80]))  # Output: Average Score is  90.0
print("Average Score is ", calc_average([70, 75, 80, 85]))  # Output: Average Score is  77.5

