# List of strings
words = ["hello", "world", "python", "lambda"]

# Using lambda to reverse each string
reversed_words = list(map(lambda x: x[::-1], words))

print("Reversed strings:", reversed_words)
