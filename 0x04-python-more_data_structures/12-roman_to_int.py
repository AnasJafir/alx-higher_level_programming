#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    total = 0
    chars_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    length = len(roman_string)

    for i in range(length):
        current_value = chars_values.get(roman_string[i], 0)

        if i + 1 < length:
            next_value = chars_values.get(roman_string[i + 1], 0)
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value

    return total
