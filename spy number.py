# Check Spy number

# Taking input
num = int(input("Enter a number: "))

# Initialize sum and product
sum = 0
product = 1

# Store original number
temp = num

# Loop to calculate sum and product
while temp > 0:
    digit = temp % 10
    sum += digit
    product *= digit
    temp //= 10

# Check Spy number
if sum == product:
    print(num, "is a Spy number")
else:
    print(num, "is not a Spy number")
