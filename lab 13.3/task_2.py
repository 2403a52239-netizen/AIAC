
def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")

#example usage
print(read_file("example.txt"))  # Replace "example.txt" with your file path