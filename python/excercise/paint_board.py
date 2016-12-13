# paint N board. can't be more than 2 consecutive color

class Board:
    def __init__(self, color, level = None):
        assert color in ('B', 'W')
        self.color = color
        self.level = level


# preordering DFS
def paint(N):
    stack = []
    seq = [None] * N
    stack.append(Board('B', 0))
    stack.append(Board('W', 0))
    while len(stack) > 0:
        current = stack.pop()
        # process current, if can_paint, push stack
        if (can_paint(seq, current)):
            seq[current.level] = current
            next_level = current.level + 1
            if next_level < N:
                stack.append(Board('B', current.level + 1))
                stack.append(Board('W', current.level + 1))
            else:
                print(''.join([b.color for b in seq]))
        else:
            continue


def can_paint(seq, current):
    if current.level >= 2 and seq[current.level - 1].color == current.color and seq[current.level - 2].color == current.color:
        return False
    else:
        return True


paint(10)
