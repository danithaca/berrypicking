#
# Contiguous Integer Subsequence
#
# Input: list[int], target int
# All integers positive >0
# output: boolean, subsequence sum exists
#
# Examples:
# [1, 2, 3], 5 -> True
# [1, 3, 2, 6], 5 -> True
# [1, 2, 3, 1000], 5 -> True
# [1, 2, 3], 4 -> False
#
# [7, 3, 3, 1, 1, 1, 1, 1], 5 => True
# [2, 2, 1, 6 ], 5 => True
# [1, 2, 2, 1, 6 ], 5 => True
#
# idea: outer loop: starts with each integer in list. inner loop: peek the next few ints.

# current solution: https://rafal.io/posts/contigous-subsequence-sum.html

def detect(input_list, target_int):
    cache = set([]) # all of the subsequence sum that we've seen so far
    for pos, i in enumerate(input_list):
        if i > target_int: # 1, 2,
            continue
        elif i == target_int:
            return True
        else:
            total = 0 # 1
            for j in input_list[pos:]: # j=2, 3
                total += j # 5
                if total > target_int:
                    break
                elif total == target_int:
                    return True
                else: # when total < target_int
                    if target_int - total in cache:
                        return True
                    else:
                        cache.add(total)
    return False