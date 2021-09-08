# Two main benefits over arrays:
# - You don't need to pre-allocate space
# - Insertion is easier

class Node:
   def __init__(self, data=None, next=None):
      self.data = data
      self.next = next
   
class Linkedlist:
   def __init__(self):
      self.head = None

   def print(self):
      if self.head == None:
         print("Empty linked list")
         return

      itr = self.head
      ll_string = ''

      while itr != None:
         if itr.next == None:
            ll_string += str(itr.data)
            break
        
         ll_string += str(itr.data) + ' --> '
         itr = itr.next
      
      print(ll_string)


   def insert_at_begining(self, data):
      node = Node(data, self.head)
      self.head = node

   def insert_at_end(self, data):
      if self.head == None:
         self.head = Node(data, None)
         return
      
      itr = self.head
      while itr.next != None:
         itr = itr.next
      
      itr.next = Node(data, None)

   # Will 'erase' the previous linked list and create another one from sketch
   def insert_values(self, data_list):
      self.head = None
      for data in data_list:
         self.insert_at_end(data)

   def get_length(self):
      count = 0
      itr = self.head
      while itr != None:
         count += 1
         itr = itr.next
      
      return count

   def remove_at(self, index):
      if index < 0 or index >= self.get_length():
         raise Exception("Invalid index")
      
      if index == 0:
         self.head = self.head.next
         return

      count = 0
      itr = self.head
      while itr != None:
         if count == index - 1:
            itr.next = itr.next.next
            break

         itr = itr.next
         count += 1

   def insert_at(self, index, data):
      if index < 0 or index >= self.get_length():
         raise Exception("Invalid index")

      if index == 0:
         self.insert_at_begining(data)
         return

      count = 0
      itr = self.head
      while itr != None:
         if count == index - 1:
            node = Node(data, itr.next)
            itr.next = node
            break

         itr = itr.next
         count += 1 

      
if __name__ == '__main__':

   ll = Linkedlist()

   # ll.insert_at_begining(15)
   # ll.insert_at_begining(3)
   # ll.insert_at_end(9)

   ll.insert_values(["banana", "mango", "strawberries", "grapes", "apple"])

   ll.print()
   print("Length: " + str(ll.get_length()))

   # ll.remove_at(2)

   ll.insert_at(2, "passion fruit")

   ll.print()
   print("Length: " + str(ll.get_length()))
