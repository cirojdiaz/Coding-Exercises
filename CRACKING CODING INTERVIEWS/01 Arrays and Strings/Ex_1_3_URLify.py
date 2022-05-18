# Replace spaces, empty spaces at the enf gone

def replace_empty(myStr: str, w='%20'):
    # Remove empty characters at the end
    for n in range(len(myStr)-1, 0, -1):
        if myStr[n] == ' ':
            myStr = myStr[:-1]
        else:
            break

    # Substitute inner empty characters
    str_lst = ''
    for n in range(len(myStr)):
        if myStr[n] == ' ':
            str_lst += w
        else:
            str_lst += myStr[n]
    return str_lst


s = 'a space replaced    '
print('String "{}", and string replaced "{}"'.format(s, replace_empty(s)))
