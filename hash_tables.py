# A key value is linked to another value by a Hash Function
# Look up by key is O(1) on average and Insertion/Deletion is also O(1) on average

class HashTable:
   def __init__(self):
      self.MAX = 100
      self.arr = [None for i in range(self.MAX)]

   # This function will generate an index between 0 and 99 based on what you pass as key. Ex: 'march 6' -> index of 9
   def get_hash(self, key):
      h = 0
      for char in key:
         h += ord(char)
      return h % self.MAX

   # This function add elements to the HT, first it generates an index based on the key, and then stores the value on that index
   def add(self, key, value):
      h = self.get_hash(key)
      self.arr[h] = value

   def __setitem__(self, key, value):
      h = self.get_hash(key)
      self.arr[h] = value

   # Returns the value based on the inserted key
   def get(self, key):
      h = self.get_hash(key)
      return self.arr[h]

   def __getitem__(self, key):
      h = self.get_hash(key)
      return self.arr[h]

   # Deletes the value correspondent to the inserted key
   def delete(self, key):
      h = self.get_hash(key)
      self.arr[h] = None

   def __delitem__(self, key):
      h = self.get_hash(key)
      self.arr[h] = None


if __name__ == '__main__':

   ht = HashTable()

   ht.add('march 6', 130)
   ht['dec 17'] = 980
   ht['feb 4'] = 55
   ht['feb 6'] = 340

   ht.delete('feb 6')
   del ht['dec 17']

   print(ht.get('march 6'))
   print(ht['dec 17'])
   print(ht['feb 4'])
   print(ht['feb 6'])
