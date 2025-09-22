#refactor the code using list comprehension instead of for loop
import time
start = time.time()

squares = [i**2 for i in range(1, 1000000)]  # List comprehension directly on range

print(len(squares))

end = time.time()
print("Time taken:", end - start)