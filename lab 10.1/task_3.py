#refactor the code into readable names with inline comments
def calculate_percentage(x,y):    #calculate percentage
 return x*y/100    #formula for percentage

amount=200
rate=15
print(calculate_percentage(amount,rate))  # Output: 30.0
#test cases
print(calculate_percentage(150,10))  # Output: 15.0
print(calculate_percentage(500,20))  # Output: 100.0
