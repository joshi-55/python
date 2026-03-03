# Check perfect number

# Taking input
num = int(input("Enter a number: "))

# Variable to store sum of divisors
sum = 0

# Finding divisors
for i in range(1, num):
    if num % i == 0:
        sum += i

# Checking perfect number
if sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
