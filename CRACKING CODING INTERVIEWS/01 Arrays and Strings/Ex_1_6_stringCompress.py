# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed"string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompress(myStr: str):
    # all leters to lower case
    myStr = myStr.lower()

    last = myStr[0]
    newStr = last
    freq = 1
    for e in myStr[1:]:
        if e == last:
            freq += 1
        else:
            newStr += str(freq) * (freq > 1)
            freq = 1
            last = e
            newStr += e
    newStr += str(freq) * (freq > 1)
    return newStr

s = 'aabbbccccaa'
print('The string "{}" is compressed {}'.format(s, stringCompress(s)))