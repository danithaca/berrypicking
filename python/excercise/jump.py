# https://leetcode.com/problems/frog-jump/

stones = [0,1,3,5,6,8,12,17]

def can_jump(stones):
    previous_k = 0
    for pos in range(len(stones) - 1):
        k = stones[pos + 1] - stones[pos]
        if k in (previous_k, previous_k-1, previous_k+1):
            # jump
            print('Jump:', stones[pos], stones[pos+1])
            previous_k = k
        else:
            print('Position', pos)
            return False
    return True

print(can_jump(stones))
