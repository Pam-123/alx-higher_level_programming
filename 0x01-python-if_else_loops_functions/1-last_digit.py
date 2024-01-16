#!/usr/bin/python3
import random

# Generate a random signed number in the range of -10000 to 10000
number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10  # Taking the absolute value to handle negative numbers

# Print the information about the last digit
print("Last digit of", number, "is", last_digit, end=' ')

# Check conditions based on the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
