def add(a, b):
    """
    Add two numbers together.

    Parameters
    ----------
    a : float
        First number to add.
    b : float
        Second number to add.

    Returns
    -------
    float
        The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtract the second number from the first number.

    Parameters
    ----------
    a : float
        Number to subtract from.
    b : float
        Number to subtract.

    Returns
    -------
    float
        The result of a - b.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers together.

    Parameters
    ----------
    a : float
        First number to multiply.
    b : float
        Second number to multiply.

    Returns
    -------
    float
        The product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Divide the first number by the second number.

    Parameters
    ----------
    a : float
        Dividend (number to be divided).
    b : float
        Divisor (number to divide by).

    Returns
    -------
    float
        The quotient of a and b.

    Raises
    ------
    ValueError
        If b is zero (division by zero).
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Example usage and testing
if __name__ == "__main__":
    try:
        # Get user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform calculations
        print(f"Addition: {add(num1, num2)}")
        print(f"Subtraction: {subtract(num1, num2)}")
        print(f"Multiplication: {multiply(num1, num2)}")
        print(f"Division: {divide(num1, num2)}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")