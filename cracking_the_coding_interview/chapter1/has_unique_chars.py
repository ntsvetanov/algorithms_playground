def has_unique_chars(string):
    
    characters = {}
    for ch in string:
        if ch  in characters.keys():
            return False
        else:
            characters[ch] = 1
    return True
def has_unique_chars_without_dict(string):
    
    for i, ch in enumerate(string):
        for next_ch in string[i + 1:]:
            if ch == next_ch:
                return False
    return True
