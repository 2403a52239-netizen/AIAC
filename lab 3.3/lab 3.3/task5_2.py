def convert_temp(value, direction):
    """
    Convert temperature between Celsius and Fahrenheit.

    Args:
        value (float or int): The temperature value to convert.
        direction (str): 'C to F' to convert Celsius to Fahrenheit,
                         'F to C' to convert Fahrenheit to Celsius.

    Returns:
        float: The converted temperature.

    Raises:
        ValueError: If direction is invalid or value is not a number.
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Temperature value must be a number.")
    direction = direction.strip().upper()
    if direction == 'C TO F':
        return value * 9/5 + 32
    elif direction == 'F TO C':
        return (value - 32) * 5/9
    else:
        raise ValueError("Direction must be 'C to F' or 'F to C'.")
if __name__ == "__main__":
    try:
        temp = float(input("Enter the temperature value: "))
        direction = input("Enter conversion direction ('C to F' or 'F to C'): ")
        converted = convert_temp(temp, direction)
        print(f"Converted temperature: {converted:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


