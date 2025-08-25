def calculate_factorial():
    try:
        num = int(input("Enter a non-negative integer: ").strip())
        if num < 0:
            print("Inappropriate input: number must be non-negative.")
            return
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        print(f"Factorial of {num} is {factorial}.")
    except ValueError:
        print("Inappropriate input: please enter a valid integer.")

calculate_factorial()
