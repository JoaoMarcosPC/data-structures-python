# A modified version of the binary search tree that provides more efficient lookup, insertion and deletion operations
# Basically is a binary search tree with a built-in self-balancing feature
# Balancing is performed after certain insertion and deletion operations

class TreeNode():
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      self.height = 1

class AVLTree():
   def insert(self, root, data):
      if not root:
         return TreeNode(data)
      elif data < root.data:
         root.left = self.insert(root.left, data)
      else:
         root.right = self.insert(root.right, data)
      
      balanceFactor = self.getBalance(root)

      if balanceFactor > 1:
         if self.getBalance(root,left) >= 0:
            return self.rigthRotate(root)
         else:
            root.left = self.leftRotate(root.left)
            return self.rigthRotate(root.left)
      if balanceFactor < -1:
         if self.getBalance(root.right) <=0:
            return self.leftRotate(root)
         else:
            root.right = self.rigthRotate(root.right)
            return self.leftRotate(root)
      
      return root
   
   def leftRotate(self, root):
      y = root.right
      T2 = y.left
      y.left = root
      root.right = T2

      root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
      y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

      return y

   def rigthRotate(self, root):
      y = root.left
      T3 = y.right
      y.right = root
      root.left = T3

      root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
      y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

      return y

   def getBalance(self, root):
      if root == None:
         return 0
      return self.getHeight(root.left) - self.getHeight(root.right)

   def getHeight(self, root):
      if root == None:
         return 0
      return root.height


if __name__ == '__main__':
   avl_tree = AVL()
   nums = [33, 13, 52, 9, 21, 61, 8, 11]
   root=None
   for num in nums:
      avl_tree.insert(root, num)