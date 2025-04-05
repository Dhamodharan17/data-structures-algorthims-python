

class LLNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    
    def insert_at_end(self,data):
        
        temp = self.head
        if temp is None:
            self.head = LLNode(data)
            return
        
        while temp.next:
            temp = temp.next
        
        temp.next = LLNode(data)
    
    def print(self):
        
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def delete_at_start(self):
        self.head = self.head.next
    
        
    def delete_at_end(self):
        
        if not self.head:
            print("empty list cannot delete")
            return
        
        if not self.head.next:
            head = None
            return
        
        temp = self.head
        #stop at last second Node
        while temp.next.next:
            temp = temp.next
        
        temp.next = None
        
    
    def delete_at_pos(self, pos):
        
        if pos == 1:
            self.head = self.head.next
            return
        
        temp = self.head
        count = 1
        while temp and count < pos-1:
            count += 1
            temp = temp.next
        
        if not temp or not temp.next:
            print("out of bound")
            return
        
        temp.next = temp.next.next 
        
        
        
    def delete_at_before(self,before):
        
        if self.head is None:
            return
        
        #delete head case
        if self.head.next.data == before:
            self.head = self.head.next
            return
        
        #why prev? 20 30 40 50 60
        # to delete before 50 i.e 40 -> we will stop at 40, but we need its prev
        temp = self.head
        prev = None
        while temp.next and temp.next.data != before:
            prev = temp
            temp = temp.next
        
        if not temp or not temp.next:
            print("out of bound")
            return
        
        prev.next = temp.next
        
        
        
        
    def delete_at_after(self,after):
    
        
        temp = self.head
        while temp and temp.data != after:
            temp = temp.next
       
        if not temp or not temp.next:
            return
         # when next not exists, will raise exception
        temp.next = temp.next.next
        
   

#call
ll = LinkedList()

ll.insert_at_end(31)
ll.insert_at_end(32)
ll.insert_at_end(33)
ll.insert_at_end(34)

# ll.delete_at_start()
# ll.delete_at_end()
# ll.delete_at_pos(2)
# ll.insert_at_end(32)
# ll.delete_at_pos(1)
# ll.insert_at_end(31)
# ll.delete_at_pos(4)
#ll.delete_at_before(32)
ll.delete_at_after(31)
ll.print()
    
        
    
    
    
    
        
        
