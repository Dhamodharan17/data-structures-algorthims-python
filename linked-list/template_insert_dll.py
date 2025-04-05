
class DLLNode:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.nxt = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self,x):
        #logic
        
       
    def insert_at_end(self,x):
        #logic
        
       
        
    def insert_at_pos(self,pos,x):
        #logic
        
    def insert_before_node(self,before,x):
        #logic
        
       
    
        
    def insert_after_node(self,after,x):
        #logic
       
    
    def print(self):
        
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.nxt
      
dll = DoublyLinkedList()
dll.insert_at_start(1)
dll.print()
      
