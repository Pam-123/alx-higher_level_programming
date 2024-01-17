#!/usr/bin/python3

# Loop for the tens place (first digit)
for tens in range(10):
    # Loop for the units place (second digit)
    for units in range(tens + 1, 10):
        # Print the combination as two-digit numbers
        print("{:d}{:d}".format(tens, units), end=', ' if tens != 8 or units != 9 else '\n')
