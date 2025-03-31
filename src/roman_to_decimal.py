def roman_to_decimal(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman.upper()):
        value = roman_values.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

# Example usage
# roman_numeral = input("Enter a Roman numeral: ")
# decimal = roman_to_decimal(roman_numeral)
# print(f"Decimal value of {roman_numeral} is {decimal}")

