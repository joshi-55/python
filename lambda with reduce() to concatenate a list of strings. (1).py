from functools import reduce
words = ["Hello", " ", "World", "!"]
result = reduce(lambda x, y: x + y, words)
print("Concatenated String:", result)
