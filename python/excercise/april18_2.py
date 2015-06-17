data = s.split(' ')
results = []

# this approach is to avoid confusions about big-endian and small endian
mapping = {
    '0': '    ',
    '1': '   x',
    '2': '  x ',
    '3': '  xx',
    '4': ' x  ',
    '5': ' x x',
    '6': ' xx ',
    '7': ' xxx',
    '8': 'x   ',
    '9': 'x  x',
    'A': 'x x ',
    'B': 'x xx',
    'C': 'xx  ',
    'D': 'xx x',
    'E': 'xxx ',
    'F': 'xxxx',
    }

for hex_str in data:
    # assume data is in the correct format
    assert len(hex_str) == 2
    hex_str = hex_str.upper()
    assert hex_str[0] in mapping and hex_str[1] in mapping
    # save as results, but can just print out with out saving
    output = mapping[hex_str[0]] + mapping[hex_str[1]]
    print(output)
    results.append(output)

return results