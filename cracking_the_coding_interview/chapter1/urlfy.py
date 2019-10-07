def urlify(string, str_len):
    urlfied_string = []
    ss = list(string)
    print(len(string))
    for ch in range(str_len):
        if string[ch] == " ":
            urlfied_string.append("%20")
        else:
            urlfied_string.append(string[ch])

    return "".join(urlfied_string)