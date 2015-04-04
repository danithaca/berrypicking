class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def access(self):
        print(self.data)

    def __eq__(self, other):
        try:
            return self.data == other.data
        except:
            return False


class Tree:
    def __init__(self, node):
        assert isinstance(node, Node) and node is not None
        self.head = node

    @staticmethod
    def preorder(node):
        if node is None:
            return
        node.access()
        Tree.preorder(node.left)
        Tree.preorder(node.right)

    @staticmethod
    def compare(tree_head_1, tree_head_2):
        if tree_head_1 is None or tree_head_2 is None:
            return tree_head_1 == tree_head_2
        elif tree_head_1 == tree_head_2 and Tree.compare(tree_head_1.left, tree_head_2.left) and Tree.compare(tree_head_1.right, tree_head_2.right):
            return True
        else:
            return False

    def traverse(self):
        Tree.preorder(self.head)

    def __eq__(self, other):
        return Tree.compare(self.head, other.head)


if __name__ == '__main__':
    tree1 = Tree(Node('root', Node('n1', Node('n3'), Node('n4')), Node('n2')))
    tree2 = Tree(Node('root', Node('n1', Node('n3'), Node('n4')), Node('n22')))
    tree1.traverse()
    print(tree1 == tree2)