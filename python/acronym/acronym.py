
def abbreviate(words):
    acronim = ''
    for w in words.replace('-', ' ').split():
        acronim += w[0].upper()
    return acronim