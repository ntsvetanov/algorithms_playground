def is_substring(string, sub):
    return string.find(sub) != -1

# My Solution

def string_rotation(s1, s2):
    if len(s1) == len(s2):
        return is_substring(s2+s2, s1)
    return False
print(string_rotation("waterbottle", 'erbottlewat'))
print("waterbottle" + 'erbottlewat')