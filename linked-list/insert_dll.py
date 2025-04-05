
class DLLNode:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.nxt = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self,x):
        
        newnode = DLLNode(x)
        
        if self.head is None:
            self.head = newnode
            return
        
        newnode.nxt = self.head #forward chain
        self.head.prev = newnode #backward chain
        self.head = newnode

    def insert_at_end(self,x):
        
        newnode = DLLNode(x)
        
        #stop last prev
        if self.head is None:
            self.head = newnode
            return
        
        temp = self.head
        while temp.nxt:
            temp = temp.nxt
            
        temp.nxt = newnode
        newnode.prev = temp
        
    def insert_at_pos(self,pos,x):
        newnode = DLLNode(x)
        
        #edge case - head node
        if pos == 1:
            newnode.nxt = self.head #1
            self.head.prev = newnode # 2
            self.head = newnode
            return
        
        temp = self.head
        count = 1
        while temp and count < pos-1:
            count += 1
            temp = temp.nxt
        
        if not temp:
            print("position out of bound")
            return
        
        # stop before
        newnode.nxt = temp.nxt
        newnode.prev = temp
        if temp.nxt:
            temp.nxt.prev = newnode
        temp.nxt = newnode
        
    def insert_before_node(self,before,x):
        
        newnode = DLLNode(x)
        if self.head.data == before:
            newnode.nxt = self.head
            self.head.prev = newnode
            self.head = newnode
            return
        
        temp = self.head
        while temp and temp.data != before:
            temp = temp.nxt
        
        if not temp:
            print("ip not found")
            return
        
        newnode.nxt = temp
        newnode.prev = temp.prev
        temp.prev.nxt = newnode
        temp.prev = newnode
            
    
        
    def insert_after_node(self,after,x):
        
        newnode = DLLNode(x)
        temp = self.head
        
        while temp and temp.data != after:
            temp = temp.nxt
        
        if not temp:
            print("ip not found")
            return
        
        newnode.nxt = temp.nxt
        newnode.prev = temp
        if temp.nxt:
            temp.nxt.prev = newnode
        temp.nxt = newnode
    
    def print(self):
        
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.nxt
        
        
        
dll = DoublyLinkedList()
dll.insert_at_start(1)
dll.insert_at_start(2)
dll.insert_at_start(3)
dll.insert_at_end(5)
dll.insert_at_pos(2,-1)
dll.insert_after_node(5,8)
dll.insert_before_node(3,0)
dll.insert_before_node(3,1)
dll.print()
        
