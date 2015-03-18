class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def access(self):
        print(self.data)


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

    def traverse(self):
        Tree.preorder(self.head)


if __name__ == '__main__':
    tree = Tree(Node('root', Node('n1', Node('n3'), Node('n4')), Node('n2')))
    tree.traverse()