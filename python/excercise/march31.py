def find_number(x):
    str_x = str(x)
    if len(str_x) == 1:
        raise Exception()

    left_most = str_x[0]
    try:
        small_from_rest = find_number(int(str_x[1:]))
        return int(left_most + str(small_from_rest))
    except:
        # min() will throw exception if parameter is empty list, meaning no digit is greater than the left_most digit.
        new_left_most = min([c for c in str_x[1:] if c > left_most])
        # assumption: no repeated digit
        rest_of_digits = ''.join(sorted([c for c in str_x if c != new_left_most]))
        y = new_left_most + rest_of_digits
        return int(y)

print(find_number(5346))