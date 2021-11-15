# João Marcos Peixoto Cavalcante

class Node(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, node):
        self.root = node

    def depth(self, x):
        return self._depth(x, self.root)

    def _depth(self, x, node):
        d = 0
        while(node != None and x != node.data):
            node = node.parent
            d += 1
        return d

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node == None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node == None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, node):
        elements = []

        if node.left:
            elements += self._inOrder(node.left)

        elements.append(node.data)

        if node.right:
            elements += self._inOrder(node.right)

        return elements

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, node):
        elements = []

        elements.append(node.data)

        if node.left:
            elements += self._preOrder(node.left)

        if node.right:
            elements += self._preOrder(node.right)

        return elements

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, node):
        elements = []

        if node.left:
            elements += self._postOrder(node.left)

        if node.right:
            elements += self._postOrder(node.right)

        elements.append(node.data)

        return elements
