def permute(s):
    if len(s) == 1:
        return [s]
    r = []
    for i, ss in enumerate(s):
        r.extend([ss + sss for sss in (permute(s[:i] + s[i + 1:]))])
    return r

print(permute('hatx'))