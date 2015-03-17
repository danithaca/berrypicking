# phone number permutation problem

num = {
    '1': '1',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PRS',
    '8': 'TUV',
    '9': 'WXY',
    '0': '0',
    '-': '-'
}


def gen(n):
    if len(n) == 1:
        return [n]
    r = []
    x = n[0]
    y = n[1:]
    for xx in num[x]:
        r.extend([xx + yy for yy in gen(y)])
    return r


print(gen('926-9295'))