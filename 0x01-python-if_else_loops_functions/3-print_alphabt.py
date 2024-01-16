#!/usr/bin/python3
# Author: Pamela Chawira

# Print the lowercase alphabet excluding 'q' and 'e'
for i in range(97, 123):
    if chr(i) not in ('q', 'e'):
        print("{}".format(chr(i)), end="")
