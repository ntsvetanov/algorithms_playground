def is_permutation(first_string, second_string):
    first_chars = {}
    for ch in first_string:
        if ch  in first_chars.keys():
            first_chars[ch] += 1
        else:
            first_chars[ch] = 1

    second_chars = {}
    for ch in second_string:
        if ch  in second_chars.keys():
            second_chars[ch] += 1
        else:
            second_chars[ch] = 1

    for k in  first_chars:
        try:
            if second_chars[k] != first_chars[k]:
                return False
        except:
            return False
    return True
