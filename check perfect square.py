# Check perfect square

import math

# Taking input
num = int(input("Enter a number: "))

# Finding square root
root = math.sqrt(num)

# Checking perfect square
if root == int(root):
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")
