#!/usr/bin/python3

# ASCII value for 'a'
ascii_a = ord('a')

# Print the lowercase alphabet using the .format() method
print("{}".format("".join(chr(ascii_a + i) for i in range(26))), end='')
