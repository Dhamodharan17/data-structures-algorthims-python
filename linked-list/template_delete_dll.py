
class DLLNode:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self,x):
        print('logic')
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def delete_at_start(self):
        print('logic')
    def delete_at_end(self):
        print('logic')
    def delete_at_pos(self,pos):
        print('logic')
    def delete_before_node(x):
        print('logic')
    def delete_after_node(x):
        print('logic')
        
        
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.print()
