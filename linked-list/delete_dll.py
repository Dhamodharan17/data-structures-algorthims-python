
class DLLNode:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self,x):
        
        newnode = DLLNode(x)
        
        #stop last prev
        if self.head is None:
            self.head = newnode
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = newnode
        newnode.prev = temp
    
    def print(self):
        
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def delete_at_start(self):
        
        if self.head is None:
            return
        
        #op 1
        #self.head = self.head.next
        #self.head.prev = None
        
        #op2
        self.head.next.prev = None
        self.head = self.head.next
        
    def delete_at_end(self):
        temp = self.head
        
        if temp.next is None:
            self.head = None
            return
        
        while temp.next:
            temp = temp.next
        #remove last node
        temp.prev.next = None
    
    def delete_at_pos(self,pos):
        
        if pos == 1:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
                return
            else:
                self.head = None
            
        count = 1
        temp = self.head
        
        #stop at pos
        while temp and count < pos:
            count += 1
            temp = temp.next
        
        if not temp:
            return
        # at pos, remove my coming connections
        # 1 connection from prev and another from next
        temp_prev = temp.prev
        temp.prev.next = temp.next
        temp.next.prev = temp_prev
    
    def delete_before_node(x):
        print('logic')
        
    def delete_after_node(x):
        print('logic')
        
        
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(5)
# dll.delete_at_start()
# dll.delete_at_end()
dll.delete_at_pos(3)
dll.print()

