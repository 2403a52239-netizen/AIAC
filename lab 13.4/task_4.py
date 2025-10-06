# refactor the code using dictionary mapping
operation = "multiply"
a, b = 5, 3

operations_map = {
    "add": a + b,
    "subtract": a - b,
    "multiply": a * b
}
result = operations_map.get(operation, None)
print(result)