# -> Binary trees are basically trees that have at max 2 child nodes

# -> What kind of problem a binary tree solve ?
# It can be used to implement binary search

# -> Ways to travel through a binary tree
# In order traversal - Left subtree, than root, and finally right subtree -> sort elements in ascending order
# Pre order traversal - Root, than left subtree, and finally right subtree
# Pos order traversal - Left subtree, than right subtree, and finally root

class BinarySearchTree:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
   
   def add_child(self, data):
      if data == self.data:
         return
      
      if data < self.data:
         if self.left:
            self.left.add_child(data)
         else:
            self.left = BinarySearchTree(data)
      else:
         if self.right:
            self.right.add_child(data)
         else:
            self.right = BinarySearchTree(data)

   def in_order_traversal(self):
      elements = []

      # visit left tree
      if self.left:
         elements += self.left.in_order_traversal()

      # visit root node
      elements.append(self.data)

      #visit right tree
      if self.right:
         elements += self.right.in_order_traversal()

      return elements

   def search(self, val):
      if self.data == val:
         return True
      
      if val < self.data:
         if self.left:
            return self.left.search(val)
         else:
            return False

      if val > self.data:
         if self.right:
            return self.right.search(val)
         else:
            return False
   
   def find_min(self):
      if self.left == None:
         return self.data
      return self.left.find_min()

   def find_max(self):
      if self.right == None:
         return self.data
      return self.right.find_max()
   
   # Substitutes the deleted element by the min of the right subtree of that element
   def delete_right(self, val):
      # Will search element in the tree
      if val < self.data:
         if self.left:
            self.left = self.left.delete_right(val)
      elif val > self.data:
         if self.right:
            self.right = self.right.delete_right(val)
      else:
         # Adjusts it's child elements
         if self.left is None and self.right is None:
            return None
         if self.left is None:
            return self.right
         if self.right is None:
            return self.left

         # Changes value
         min_val = self.right.find_min()
         self.data = min_val
         self.right = self.right.delete_right(min_val)

      # The value is returned no matter if is the value we're searching for or not
      return self

   # Substitutes the deleted element by the max of the left subtree of that element
   def delete_left(self, val):
      if val < self.data:
         if self.left:
            self.left = self.left.delete_right(val)
      elif val > self.data:
         if self.right:
            self.right = self.right.delete_right(val)
      else:
         if self.left is None and self.right is None:
            return None
         if self.left is None:
            return self.right
         if self.right is None:
            return self.left
         
         max_value = self.left.find_max()
         self.data = max_value
         self.left = self.left.delete_left(max_value)
      
      return self

def build_tree(elements):
   root = BinarySearchTree(elements[0])

   for i in range(1, len(elements)):
      root.add_child(elements[i])

   return root
   

if __name__ == '__main__':

   numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
   numbers_tree = build_tree(numbers)
   print("Original tree:", numbers_tree.in_order_traversal())
   numbers_tree.delete_right(9)
   numbers_tree.delete_left(20)
   print(numbers_tree.in_order_traversal())
   print(numbers_tree.search(20))
   print(numbers_tree.search(8))

   countries = ["India", "Pakistan", "Germany", "USA", "China", "Australia", "India", "UK", "USA"]
   country_tree = build_tree(countries)
   print(country_tree.in_order_traversal())
   print("UK is on the list ?", country_tree.search("UK"))
   print("Sweden is on the list ?", country_tree.search("Sweden"))
