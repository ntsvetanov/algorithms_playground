def is_armstrong_number(number):
    str_number = str(number)
    return sum([pow(int(digit), len(str_number)) for digit in str_number]) == number

