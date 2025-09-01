def print_multiples_for(number):
    print(f"First 10 multiples of {number} using for loop:")
    for i in range(1, 11):
        print(number * i)

number = int(input("Enter a number: "))
print_multiples_for(number)