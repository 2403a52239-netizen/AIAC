def sum_to_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    print("Sum from 1 to", n, "is", sum_to_n_for(n))