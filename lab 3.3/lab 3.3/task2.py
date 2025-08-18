def sort_list(arr):
    """
    Sorts a list of numbers in ascending order using the built-in sorted function.

    Args:
        arr (list): List of numbers to sort.

    Returns:
        list: Sorted list of numbers.
    """
    return sorted(arr)

# Example usage
if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    sorted_numbers = sort_list(numbers)
    print("Original list:", numbers)
    print("Sorted list:", sorted_numbers)
