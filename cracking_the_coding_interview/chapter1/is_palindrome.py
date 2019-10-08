

def is_palindome(string):
    string = string.lower().replace(" ", "")

    characters = {}
    for ch in string:
        if ch  in characters.keys():
            if  characters[ch] > 0:
                 characters[ch] -= 1
            else:
                characters[ch] = 1
        else:
            characters[ch] = 1

    not_palindrome = False
    
    for i in list(characters.values()):
        if not_palindrome:
            return False

        if i == 1 :
            not_palindrome = True

    return True


data = [ ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

for i in data:
    if is_palindome(i[0]) != i[1]:
        print("error ")
