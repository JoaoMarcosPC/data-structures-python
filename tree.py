# Trees can be considered an recursive data structure

class Tree:
   def __init__(self, data):
      self.data = data
      self.children = []
      self.parent = None

   def add_node(self, child):
      child.parent = self
      self.children.append(child)

   def get_level(self):
      level = 0
      parent = self.parent

      while parent:
         parent = parent.parent
         level += 1

      return level

   def print_tree(self):
      spaces = ' ' * self.get_level() * 5
      if self.parent:
         prefix = spaces + '|__'
      else:
         prefix  = spaces

      print(prefix + self.data)

      if len(self.children) > 0:
         for child in self.children:
            child.print_tree()

def build_product_tree():
   root = Tree("Electronics")

   laptop = Tree("Laptop")
   laptop.add_node(Tree("Mac"))
   laptop.add_node(Tree("PC"))
   laptop.add_node(Tree("ThinkPad"))

   cellphone = Tree("Cellphone")
   cellphone.add_node(Tree("Android Phone"))
   cellphone.add_node(Tree("IPhone"))

   root.add_node(laptop)
   root.add_node(cellphone)

   root.print_tree()

if __name__ == '__main__':
   build_product_tree()
