
class LLNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        newnode = LLNode(data)
        if self.head:
            newnode.next = self.head
            self.head = newnode
            return
        else:
            self.head = newnode
            
        print("Insertion at Head")
    
    def insert_at_end(self,data):
        
        if self.head is None:
            self.head = LLNode(data)
            return
        
        def helper(temp):
            if temp is None:
              return LLNode(data)
            
            temp.next = helper(temp.next)
            return temp
            
        helper(self.head)
        print("Insertion at End")
    
    def insert_at_pos(self, data, pos):
    
        newnode = LLNode(data)
        
        def helper(temp, k):
            #each the node just before the position
            if k == 1:
                newnode.next = temp
                return newnode
            #temp.next = newnode
            temp.next = helper(temp.next, pos-1)
            return temp
        
        self.head = helper(self.head, pos)
        print("Insertion at POS")
        
    def insert_at_after(self,data,after):
        
        newnode = LLNode(data)
        def helper(temp):
            
            if temp is None:
                return None
            if temp.data == after:
                newnode.next = temp.next
                temp.next = newnode #after
                return temp
            temp.next = helper(temp.next)
            
            return temp
        
        self.head = helper(self.head)    
        print("Insertion at After")
        
    def insert_at_before(self,data,before):
        
        newnode = LLNode(data)
        def helper(cur, prev):
            
            if cur is None:
                return None
            
            if cur.data == before:
                newnode.next = cur #insert before
                if prev: 
                    prev.next = newnode
                    return newnode
                else:
                    return newnode #head
                    
            cur.next = helper(cur.next, cur)
            return cur
        
        self.head = helper(self.head, None)
        print("Insertion at After")
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

#call
ll = LinkedList()
# ll.insert_at_start(21)
ll.insert_at_end(22)
ll.insert_at_pos(23,2)
ll.insert_at_after(22,23)
ll.insert_at_before(24,23)
ll.print()
