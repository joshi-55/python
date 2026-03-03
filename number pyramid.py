# Number Pyramid

# Taking input
n = int(input("Enter number of rows: "))

# Loop for rows
for i in range(1, n + 1):
    
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print numbers
    for k in range(1, i + 1):
        print(k, end=" ")
    
    # Move to next line
    print()
