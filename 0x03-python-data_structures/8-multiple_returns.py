def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    if length == 0:
        first_char = 0
    return length, first_char
