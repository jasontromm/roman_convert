from roman_to_decimal import roman_to_decimal

# Example usage
def main () :
    roman_numeral = input("Enter a Roman numeral: ")
    try:
        decimal = roman_to_decimal(roman_numeral)
    except Exception as e:
        print (e)
        return
    
    print(f"Decimal value of {roman_numeral} is {decimal}")

main()
