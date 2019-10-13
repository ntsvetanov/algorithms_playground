

def string_compression(string):

    cnt = 1
    cc = ""
    for first, nx in zip(string, string[1:] ):
       
        if first == nx:
            cnt += 1
        else:
            cc += "{}{}".format(first, cnt)
            cnt = 1

    cc += "{}{}".format(string[-1], cnt)
    if len(cc) >= len (string):
        return string
    else:
        return cc

print(string_compression("aabcccccaaf"))

data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]
