# João Marcos Peixoto Cavalcante

from BinaryTree import Node
from BinarySearchTree import BinarySearchTree


class AVLTree(BinarySearchTree):
    def __init__(self, node):
        self.root = node

    def addAVL(self, x):
        return self._addAVL(x, self.root)

    def _addAVL(self, x, node):
        if not node:
            return Node(x)
        elif x < node.data:
            node.left = self._addAVL(x, node.left)
        elif x > node.data:
            node.right = self._addAVL(x, node.right)

        fatorBal = self.getFatorBal(node)

        if abs(fatorBal) > 1:
            return self.balance(node, fatorBal)
        return node

    def removeAVL(self, x):
        return self._removeAVL(x, self.root)

    def _removeAVL(self, x, node):
        if node == None:
            return node
        elif x < node.data:
            node.left = self._removeAVL(x, node.left)
        elif x > node.data:
            node.right = self._removeAVL(x, node.right)
        else:
            if node.left == None:
                tmp = node.right
                node = None
                return tmp
            elif node.right == None:
                tmp = node.left
                node = None
                return tmp
            tmp = self.getRightMin(node.right)
            node.data = tmp.data
            node.right = self._removeAVL(tmp.data, node.right)

        if node == None:
            return node

        fatorBal = self.getFatorBal(node)

        if abs(fatorBal) > 1:
            return self.balance(node, fatorBal)
        return node

    def postOrderIter(self):
        return self._postOrderIter(self.root)

    def _postOrderIter(self, node):
        if node == None:
            return

        pPrint = []
        p1 = []
        p2 = []

        p1.append(node)

        while p1 != []:
            node = p1.pop()
            p2.append(node)

            if node.left:
                p1.append(node.left)
            if node.right:
                p1.append(node.right)

        while p2 != []:
            node = p2.pop()
            pPrint.append(node.data)

        return pPrint

    def getFatorBal(self, node):
        if node == None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def balance(self, node, y):
        if y > 1:
            if self.getFatorBal(node.left) >= 0:
                # esq esq
                return self.rigthRotate(node)
            elif self.getFatorBal(node.left) < 0:
                # esq dir
                node.left = self.leftRotate(node.left)
                return self.rigthRotate(node)

        if y < -1:
            if self.getFatorBal(node.right) <= 0:
                # dir dir
                return self.leftRotate(node)
            elif self.getFatorBal(node.right) > 0:
                # dir esq
                node.right = self.rigthRotate(node.right)
                return self.leftRotate(node)

    def leftRotate(self, node):
        y = node.right
        node.right = y.left
        y.left = node
        return y

    def rigthRotate(self, node):
        y = node.left
        node.left = y.right
        y.right = node
        return y
