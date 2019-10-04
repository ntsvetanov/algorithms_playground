def square(number):
    if number < 1 or number > 64:
        raise ValueError("wrong number")

    if number == 1:
        return number
    
    return square(number - 1) * 2

def total(number):
    if number < 1 or number > 64:
        raise ValueError("wrong number")

    return sum([square(i) for i in range(1, number + 1)])