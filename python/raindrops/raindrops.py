
def convert(number):
    converted_number = ""
    has_divisor = False
    if number % 3 == 0:
        converted_number += "Pling"
        has_divisor = True
    if number % 5 == 0:
        converted_number += "Plang"
        has_divisor = True
    if number % 7 == 0:
        converted_number += "Plong"
        has_divisor = True
    if not has_divisor :
        converted_number = converted_number + str(number)

    return converted_number
