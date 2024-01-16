#!/usr/bin/python3
import random

# Generate a random signed number in the range of -10 to 10
number = random.randint(-10, 10)

# Print the randomly generated number
print(number, end=' ')

# Check if the number is positive, negative, or zero
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
