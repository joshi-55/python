# Check Armstrong number

# Taking input
num = int(input("Enter a number: "))

# Store original number
temp = num
order = len(str(num))
sum = 0

# Calculate sum of powers
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
