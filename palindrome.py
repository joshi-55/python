# Check palindrome number

# Taking input
num = int(input("Enter a number: "))

# Store original number
temp = num
reverse = 0

# Reverse number
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

# Check
if reverse == num:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
