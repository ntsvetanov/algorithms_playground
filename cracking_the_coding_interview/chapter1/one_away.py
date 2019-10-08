
def one_away(first_string, second_string):

    first_len = len(first_string)
    second_len = len(second_string)
    len_difference = abs(first_len - second_len)
    if len_difference >= 2:
        return False

    chars = {}
    for i in first_string:
        if i not in chars:
            chars[i] = 1 
        else:
            chars[i] += 1
        
    second_chars = {}
    for i in second_string:
        if i not in second_chars:
            second_chars[i] = 1 
        else:
            second_chars[i] += 1

     
    return len(set(chars)-set(second_chars)) <  2 and len(set(second_chars)-set(chars)) <  2

data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]


for i in data:
    if one_away(i[0],i[1]) != i[2]:
        print("error")
    else:
        print("ok")