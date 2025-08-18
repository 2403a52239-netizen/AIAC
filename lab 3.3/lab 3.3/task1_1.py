def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using iteration.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

    # Example usage of the factorial function
print(factorial(5))  # Output: 120
