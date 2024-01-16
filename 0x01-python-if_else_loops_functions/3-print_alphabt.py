#!/usr/bin/python3

# Print the lowercase alphabet excluding 'q' and 'e'
print("{}".format(
    "".join(chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in ('q', 'e'))
), end='')
