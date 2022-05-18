# String is unique?

def is_unique(s: str):
    if len(s) > 128:
        return False
    else:
        char_set = set()
        for c in s:
            if c in char_set:
                return False
            else:
                char_set.add(c)
    return True


s = 'MyLove is just you'
print('String "{}" is {} unique'.format(s,  'Not'*(not is_unique(s))))
# Note: Multiply string by boolean gives you the string if true or empty string if False
