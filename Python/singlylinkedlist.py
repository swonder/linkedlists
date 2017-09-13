class node:
   def __init__(self, d):
      self.data = d
      self.next = None
 
class linkedList:
   def __init__(self):
      self.head = None
 
   def exists(self, value):
      if self.head == None:
         return False
      n = self.head
      while True:
         if n.data == value:
            return True
         if n.next == None:
            break
         n = n.next
      return False
 
   def insert(self, value):
      oldhead = self.head
      n = node(value)
      self.head = n
      n.next = oldhead
 
   def delete(self, value):
      if not self.exists(value):
         print("delete(): '" + str(value) + "' does not exist")
         return
      prevnode = None
      n = self.head
      while True:
         if n.data == value:
            nextnode = n.next
            if prevnode != None: 
               prevnode.next = nextnode
            else:
               self.head = nextnode
         if n.next == None:
            break
         prevnode = n
         n = n.next
 
   def retrieve(self, value):
      if not self.exists(value):
         return None
      n = self.head
      while True:
         if n.data == value:
            return n
         if n.next == None:
            break
         n = n.next
 
   def size(self):
      total = 0
      if self.head == None:
         return 0
      n = self.head
      while True:
         total += 1
         if n.next == None:
            break
         n = n.next
      return total

   def displayNodes(self):
       s = ""
       if self.size() <= 0:
          return s
       n = self.head
       i = 1
       while True:
          s += str(i) + ":" + str(n.data) + " "
          if n.next == None:
             break
          n = n.next
          i += 1
       s = s[:-1]
       return s	

   def __str__(self):
       s = ""
       n = self.head
       while True:
          s += str(n.data) + "->"
          if n.next == None:
             break
          n = n.next
       s= s[:-2]
       return s
   
