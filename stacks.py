# Push(add) or pop(remove) an element -> O(1)
# Search for element -> O(n)

list_stack = []

list_stack.append('bear')
list_stack.append('wolf')
list_stack.append('tiger')
list_stack.append('shark')

# pop() -> return the last element added to the stack
# print(list_stack.pop())

# If you simply want to know which element is on top of the stack
# print(list_stack[-1])
# LIFO -> Last In First Out

# ------ However using lists as stacks in  Python is not ideal, so instead, is preferable to use deque -------
from collections import deque

class Stack:
   def __init__(self):
      self.container = deque()

   def push(self, val):
      self.container.append(val)

   def pop(self):
      return self.container.pop()

   def peek(self):
      return self.container[-1]
   
   def isEmpty(self):
      return len(self.container) == 0
   
   def size(self):
      return len(self.container)

zoo = Stack()

zoo.push('lion')
zoo.push('zebra')
zoo.push('rhino')

print(zoo.pop())

print(zoo.peek())