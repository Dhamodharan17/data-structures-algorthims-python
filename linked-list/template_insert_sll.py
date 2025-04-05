

class LLNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    
    def insert_at_start(self,data):
        #print
    def insert_at_end(self,data):
        #print
        
       
    
    def insert_at_pos(self, data, pos):
        #print
        
        
    
    def insert_at_after(self,data,after):
        #print
        
       
        
    def insert_at_before(self,data,before):
        #print
        
    def print(self):
        
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


#call
ll = LinkedList()

ll.insert_at_before(21,99)
ll.print()
