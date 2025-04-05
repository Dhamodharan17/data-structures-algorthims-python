

class LLNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    
    def insert_at_start(self,data):
        
        newNode = LLNode(data)
        newNode.next = self.head
        self.head = newNode
    
    def insert_at_end(self,data):
        
        temp = self.head
        if temp is None:
            self.head = LLNode(data)
            return
        
        while temp.next:
            temp = temp.next
        
        temp.next = LLNode(data)
    
    def insert_at_pos(self, data, pos):
        
        newNode = LLNode(data)
        
        #insert at head
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
            return
        
        temp = self.head    
        count = 1 #already at head
        while temp and count < pos - 1: #run for condition
            temp = temp.next
            count += 1
        
        if not temp:
            print("out of bound position")
            return
        
        newNode.next = temp.next
        temp.next = newNode
    
    def insert_at_after(self,data,after):
        
        temp = self.head
        
        while temp and temp.data != after:
            temp = temp.next
        
        if not temp:
            print("given node not found")
            return
        
        newNode = LLNode(data)
        newNode.next = temp.next
        temp.next = newNode
        
    def insert_at_before(self,data,before):
        
        newNode = LLNode(data)
         
        #edge case - head
        if before == self.head.data:
            newNode.next = self.head
            self.head = newNode
            return
            
        
       
        temp = self.head
        while temp.next and temp.next.data != before:
            temp = temp.next
        
        if not temp.next:
            print("before not found")
            return
        
        newNode.next = temp.next
        temp.next = newNode
        
    def print(self):
        
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


#call
ll = LinkedList()

# ll.insert_at_start(20)
ll.insert_at_end(31)
ll.insert_at_start(10)
ll.insert_at_start(20)
ll.insert_at_start(30)

ll.insert_at_pos(50,2)

ll.insert_at_after(30,31)

ll.insert_at_before(9,10)

ll.insert_at_before(21,99)
ll.print()
