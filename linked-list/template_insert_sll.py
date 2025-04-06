
class LLNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        print("Insertion at Head")
    def insert_at_end(self,data):
        print("Insertion at End")
    def insert_at_pos(self, data, pos):
        print("Insertion at POS")
    def insert_at_after(self,data,after):
        print("Insertion at After")
    def insert_at_before(self,data,before):
        print("Insertion at After")
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

#call
ll = LinkedList()
ll.insert_at_before(21,99)
ll.print()
