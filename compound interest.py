# Calculate Compound Interest

# Taking input
P = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

# Calculate compound interest
A = P * (1 + r/100) ** t
CI = A - P

# Display result
print("Compound Interest =", CI)
print("Total Amount =", A)
