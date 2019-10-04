import string

def is_pangram(sentence):

    ascii_table = {}
    for ch in string.ascii_lowercase:
        ascii_table[ch] = 0

    for l in sentence.lower().replace(" ", ""):
        try:
            ascii_table.pop(l, None)
        except:
            pass

    if ascii_table:
        return False

    return True
