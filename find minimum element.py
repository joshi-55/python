from functools import reduce

# List of numbers
numbers = [10, 5, 8, 2, 15, 3]

# Using lambda with reduce to find minimum
minimum = reduce(lambda x, y: x if x < y else y, numbers)

print("Minimum element:", minimum)
