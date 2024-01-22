#!/usr/bin/python3.8
def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        # Return a tuple with length 0 and the first character as None
        return (0, None)
    else:
        # Return a tuple with length of the sentence and its first character
        return (len(sentence), sentence[0])
