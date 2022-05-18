# One Away

def one_away(s_max, s_min):
    if len(s_max) == len(s_min):
        if len([1 for e1, e2 in zip(s_max, s_min) if e1 != e2]) > 1:
            return False
        else:
            return True
    elif abs(len(s_max) - len(s_min)) > 1:
        return False
    else:
        # remove the different character
        for n in range(len(s_min)):
            if s_max[n] != s_min[n]:
                rest_max = s_max[n + 1:]
                rest_min = s_min[n:]
                if rest_max == rest_min:
                    return True
                else:
                    return False
    return True


s1 = 'pale'
s2 = 'bake'

print('String "{}" and String "{}" are {} one away'.format(s1, s2, 'NOT' * (not one_away(s1, s2))))
