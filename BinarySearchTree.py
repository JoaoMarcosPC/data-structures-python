# João Marcos Peixoto Cavalcante

from BinaryTree import Node
from BinaryTree import BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self, node):
        self.root = node

    def find(self, x):
        return self._find(x, self.root)

    def _find(self, x, node):
        if x == node.data:
            return True
        elif x < node.data and node.left:
            return self._find(x, node.left)
        elif x > node.data and node.right:
            return self._find(x, node.right)
        else:
            return False

    def add(self, x):
        return self._add(x, self.root)

    def _add(self, x, node):
        if node == None:
            return Node(x)
        elif x < node.data:
            node.left = self._add(x, node.left)
        elif x > node.data:
            node.right = self._add(x, node.right)
        return node

    def remove(self, x):
        return self._remove(x, self.root)

    def _remove(self, x, node):
        if not self.find(x):
            return None

        if x > node.data:
            node.right = self._remove(x, node.right)
        elif x < node.data:
            node.left = self._remove(x, node.left)
        else:
            # Nó folha
            if node.left == None and node.right == None:
                node = None
                return None
            # Nó possui um filho
            elif node.left == None:
                tmp = node.right
                node = None
                return tmp
            elif node.right == None:
                tmp = node.left
                node = None
                return tmp
            # Nó possui 2 filhos
            else:
                rightMin = self.getRightMin(node.right)
                node.data = rightMin.data
                node.right = self._remove(rightMin.data, node.right)
        return node

    def getRightMin(self, node):
        if node == None or node.left == None:
            return node
        return self.getRightMin(node.left)
