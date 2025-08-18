def calculate_power_bill(units):
    """
    Calculate the power bill based on the number of units consumed.
    Example slab:
        - First 100 units: $0.5 per unit
        - Next 100 units (101-200): $0.75 per unit
        - Above 200 units: $1.2 per unit
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative")
    bill = 0
    if units <= 100:
        bill = units * 0.5
    elif units <= 200:
        bill = 100 * 0.5 + (units - 100) * 0.75
    else:
        bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.2
    return bill

# Example usage
if __name__ == "__main__":
    units = int(input("Enter the number of units consumed: "))
    try:
        total_bill = calculate_power_bill(units)
        print(f"Total power bill for {units} units: ${total_bill:.2f}")
    except ValueError as e:
        print(e)
