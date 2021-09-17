# A collision happens when two keys when passed by the hash function generate the same index
# The big O of a hash table that handles collisions can be up to O(n), same as a linked list

class HashTable:
   def __init__(self):
      self.MAX = 10
      self.arr = [[] for i in range(self.MAX)]

   def get_hash(self, key):
      hash = 0
      for char in key:
         hash += ord(char)
      return hash % self.MAX

   def __setitem__(self, key, value):
      h = self.get_hash(key)
      found = False

      index = 0
      for element in self.arr[h]:
         if element[0] == key:
            self.arr[h][index] = (key, value)
            found = True
            break
         index += 1

      # index = 0
      # for element in self.arr[h]:
      #    if element[0] == key:
      #       self.arr[h][index] = (key, value)
      #       found = True
      #       break
      #    index += 1

      if not found:
         self.arr[h].append((key, value))

   def __getitem__(self, key):
      h = self.get_hash(key)
      
      for element in self.arr[h]:
         if element[0] == key:
            return element[1]

   def __delitem__(self, key):
      h = self.get_hash(key)

      for index, element in enumerate(self.arr[h]):
         if element[0] == key:
            del self.arr[h][index]


if __name__ == '__main__':

   ht = HashTable()

   # print(ht.get_hash('march 6'))
   # print(ht.get_hash('march 17'))
   # print(ht.get_hash('march 26'))

   ht['march 6'] = 100
   ht['apr 4'] = 200
   ht['march 17'] = 300
   ht['march 26'] = 400

   del ht['march 26']

   print(ht['march 17'])

   for index in range(len(ht.arr)):
      print(ht.arr[index])

