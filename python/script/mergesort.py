def merge_sort(lst):
    assert isinstance(lst, list)
    if len(lst) <= 1:
        return lst

    cut = len(lst) // 2
    left = (i for i in merge_sort(lst[:cut]))
    right = (i for i in merge_sort(lst[cut:]))

    result = []
    left_i = next(left, None)
    right_i = next(right, None)

    while right_i is not None or left_i is not None:
        if right_i is None or (left_i is not None and left_i <= right_i):
            result.append(left_i)
            left_i = next(left, None)
        elif left_i is None or (right is not None and right_i < left_i):
            result.append(right_i)
            right_i = next(right, None)
        else:
            assert False

    return result

print(merge_sort([3,6,3,7,9,102,245,23,34,53,43]))