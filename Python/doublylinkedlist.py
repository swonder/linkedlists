################################################################
# Shawn Wonder                                                 #
# 8/4/2017                                                     #
# Basic implementation of a doubly linked list data structure  # 
################################################################

class Node:
    def __init__(self, d):
        self.prev = None
        self.data = d
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None

    def exists(self, value):
        if value:
            n = self.head
            while True:
                if n.data == value:
                    return True
                if n.next == None:
                    break
                n = n.next
            return False
        else:
            print("Exists(): value not set")
            return False

    def insert(self, value):
        if value:
            oldhead = self.head
            n = Node(value)
            self.head = n
            n.next = oldhead
            if oldhead != None:
                oldhead.prev = n
        
    def delete(self, value):
        if value:
            n = self.head
            if n == None:
                print("Delete(): '" + str(value) + "' was not found in the list")
                return
            valuefound = False
            while True:
                if n.data == value:
                    valuefound = True
                    prevnode = n.prev
                    nextnode = n.next        
                    if prevnode != None:
                        prevnode.next = n.next
                    else:
                        self.head = nextnode
                    if nextnode != None:
                        nextnode.prev = n.prev
                if n.next == None:
                    break
                n = n.next
            if not valuefound:
                print("Delete(): '" + str(value) + "' was not found in the list")

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
        if n == None:
            return s
        while True:
            if n.prev != None:
                s += " Prev: " + n.prev.data
            else:
                s += " Prev: -"
            s += " Data: " + n.data
            if n.next != None:
                s += " Next: " + n.next.data + " -> \n"
            else:
                s += " Next: -"    
            if n.next == None:
                break
            n = n.next
        return s
            

