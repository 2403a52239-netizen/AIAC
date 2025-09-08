def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence (n >= 0).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    # Check for invalid input
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base case: F(0) = 0
    if n == 0:
        return 0
    # Base case: F(1) = 1
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a non-negative integer n: "))
        print(f"The {user_input}th Fibonacci number is: {fibonacci(user_input)}")
    except ValueError as e:
        print(f"Error: {e}")