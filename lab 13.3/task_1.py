#refactor the code
def area_rectangle(x, y):
    return x * y

def area_square(x):
    return x * x

def area_circle(x):
    return 3.14 * x * x

area_dispatch = {
    "rectangle": lambda x, y: area_rectangle(x, y),
    "square": lambda x, y=0: area_square(x),
    "circle": lambda x, y=0: area_circle(x)
}

def calculate_area(shape, x, y=0):
    try:
        return area_dispatch[shape](x, y)
    except KeyError:
        raise ValueError(f"Unsupported shape: {shape}")
#example usage
print(calculate_area("rectangle", 5, 10))  # Output: 50
print(calculate_area("square", 4))        # Output: 16
print(calculate_area("circle", 3))        # Output: 28.26