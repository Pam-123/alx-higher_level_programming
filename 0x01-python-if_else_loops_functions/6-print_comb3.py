#!/usr/bin/python3

# Loop for the tens place (first digit)
for tens in range(10):
    # Loop for the units place (second digit)
    for units in range(tens + 1, 10):
        # Construct the combination as a two-digit number
        combination = f"{tens}{units}"
        # Determine the end parameter based on the condition
        end_parameter = ', ' if (tens != 8 or units != 9) else '\n'
        # Print the combination
        print(combination, end=end_parameter)
