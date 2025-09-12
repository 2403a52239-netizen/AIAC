def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers from a list of integers.
    
    Args:
        numbers (list): A list of integers to process
        
    Returns:
        tuple: A tuple containing (sum_of_even_numbers, sum_of_odd_numbers)
        
    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5])
        (6, 9)
    """
    sum_even = 0
    sum_odd = 0
    
    for num in numbers:  # Iterate through each number in the list
        if num % 2 == 0:  # Check if the number is even
            sum_even += num  # Add even number to the even sum
        else:
            sum_odd += num
    
    return sum_even, sum_odd

# Get user input
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Calculate and display results
even_sum, odd_sum = sum_even_odd(numbers)
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
