def classify(number):
    if number < 1:
        raise ValueError("must be natural number")

    alqout_nums_sum = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            alqout_nums_sum += i
            if alqout_nums_sum  > number:
                return "abundant"

    if alqout_nums_sum == number:
        return "perfect"
        
    elif alqout_nums_sum  <  number:
        return "deficient"
