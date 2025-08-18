def simple_factorial(n):
    """
    Simple function to compute factorial of a non-negative integer n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
    # Example usage of the simple_factorial function
print(simple_factorial(5))  # Output: 120


