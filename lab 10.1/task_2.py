#refactor code using docstrings
def area_of_rect(length,breadth):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): Length of the rectangle
        breadth (float): Breadth of the rectangle

    Returns:
        float: Area of the rectangle
    """
    if length <= 0 or breadth <= 0:
        raise ValueError("Length and breadth must be positive")
    return length*breadth

print(area_of_rect(10,20))
#test cases
print(area_of_rect(5,15))  # Output: 75
print(area_of_rect(7,8))   # Output: 56
print(area_of_rect(12,3))  # Output: 36
