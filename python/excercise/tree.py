# traverse tree with depth first and width first


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.traversed = False
        self.level = 0

    def is_leaf(self):
        return self.left is None and self.right is None


def bfs(tree):
    fifo = list()
    fifo.append(tree)
    # traverse
    while len(fifo) > 0:
        el = fifo.pop(0)
        # access
        print(el.val)
        # add to fifo queue
        if el.left is not None:
            fifo.append(el.left)
        if el.right is not None:
            fifo.append(el.right)


# pre-ordering dfs
def dfs_pre(tree):
    stack = list()
    stack.append(tree)
    # traverse
    while len(stack) > 0:
        el = stack.pop()
        # access
        print(el.val)
        # push to stack
        if el.right is not None:
            stack.append(el.right)
        if el.left is not None:
            stack.append(el.left)


# post-ordering dfs
# the key is to have 'traversed' to mark if the node's children has been pushed to stack or not
def dfs_post(tree):
    stack = list()
    stack.append(tree)
    # traverse
    while len(stack) > 0:
        el = stack[-1]
        assert el is not None, 'Stack: ' + str(stack)
        if el.traversed:
            # access
            print(el.val)
            stack.pop()
        else:
            if el.is_leaf():
                print(el.val)
                stack.pop()
            else:
                el.traversed = True
                if el.right is not None:
                    stack.append(el.right)
                if el.left is not None:
                    stack.append(el.left)


# in-ordering dfs
# key is to have "traversed" to track whether child nodes have been processed or not.
def dfs_in(tree):
    stack = list()
    stack.append(tree)
    # traverse
    while len(stack) > 0:
        el = stack[-1]
        if el.traversed:
            # access
            print(el.val)
            stack.pop()
            # process right node
            if el.right is not None:
                stack.append(el.right)
        else:
            if el.is_leaf():
                # access
                print(el.val)
                stack.pop()
            else:
                el.traversed = True
                if el.left is not None:
                    stack.append(el.left)


# another better approach of in-order DFS traverse.
def dfs_in_2(node):
    stack = list()
    while len(stack) > 0 or node is not None:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val)
            node = node.right


# todo: not working. see wikipedia
def dfs_post_2(node):
    stack = list()
    while len(stack) > 0 or node is not None:
        if node.left is None and node.right is None:
            print(node.val)
            node = stack.pop()
            continue

        if node.right is not None:
            stack.append(node.right)
            node = node.right
        if node.left is not None:
            stack.append(node.left)
            node = node.left


# find the depth of the tree using bfs
def tree_depth(tree):
    fifo = list()
    fifo.append(tree)
    current_level = 0
    # traverse
    while len(fifo) > 0:
        el = fifo.pop(0)
        current_level = el.level
        # add to fifo queue
        if el.left is not None:
            el.left.level = current_level + 1
            fifo.append(el.left)
        if el.right is not None:
            el.right.level = current_level + 1
            fifo.append(el.right)
    return current_level


# print tree using dfs-preordering
def print_tree(tree):
    stack = list()
    stack.append(tree)
    # traverse
    while len(stack) > 0:
        el = stack.pop()
        current_level = el.level
        # access
        print('-' * 2 * current_level, el.val)

        # push to stack
        if el.right is not None:
            el.right.level = current_level + 1
            stack.append(el.right)
        elif not el.is_leaf():
            nil = Node('*')
            nil.level = current_level + 1
            stack.append(nil)

        if el.left is not None:
            el.left.level = current_level + 1
            stack.append(el.left)
        elif not el.is_leaf():
            nil = Node('*')
            nil.level = current_level + 1
            stack.append(nil)


if __name__ == '__main__':
    tree = Node('a', Node('b', Node('d', Node('f'), Node('g')), None), Node('c', None, Node('e', Node('h'), None)))
    #bfs(tree)
    #dfs_pre(tree)
    #dfs_post(tree)
    #dfs_in(tree)
    dfs_in_2(tree)
    #print("Height of tree:", tree_depth(tree))
    print_tree(tree)