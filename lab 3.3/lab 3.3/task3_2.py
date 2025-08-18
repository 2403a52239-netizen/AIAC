def calculate_power_bill(units, rate_per_unit):
    """
    Calculate the total power bill based on units consumed and rate per unit.

    Args:
        units (float): Number of electricity units consumed.
        rate_per_unit (float): Rate per unit of electricity.

    Returns:
        float: Total power bill.
    """
    if units < 0 or rate_per_unit < 0:
        raise ValueError("Units and rate per unit must be non-negative")
    return units * rate_per_unit

# Example usage
if __name__ == "__main__":
    try:
        units = float(input("Enter the number of units consumed: "))
        rate = float(input("Enter the rate per unit: "))
        total_bill = calculate_power_bill(units, rate)
        print(f"Total power bill: ${total_bill:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
