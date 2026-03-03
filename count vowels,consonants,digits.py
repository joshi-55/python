# Count vowels, consonants, and digits

# Taking input
text = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0

# Loop through each character
for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1

# Display results
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
