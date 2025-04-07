from collections import deque

class BTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    
    def __init__(self):
        self.root = None
    
    #using bfs - insert at 1st available position
    #complete binary tree
    def insert(self,x):
        
        newnode = BTNode(x)
        if self.root is None:
            self.root  = newnode
            return
        
        temp = self.root
        q = deque()
        q.append(temp)
        
        while q:
            size = len(q)
            
            for i in range(size):
                cur = q.popleft()
                
                if cur.left is None:
                    cur.left = newnode
                    return
                elif cur.right is None:
                    cur.right = newnode
                    return
                q.append(cur.left)
                q.append(cur.right)
    
    def delete(self, x):
        
        temp = self.root
        
        if self.root and self.root.data == x and not self.root.left and not self.root.right:
            self.root = None
            return
        
        found, cur = None, None
        q = deque([temp])
        
        #find the delete node
        while q:
            cur = q.popleft()
            if cur.data == x:
                found = cur
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        
        if not found:
            return
        
        #replace value in found with lastnode
        found.data = cur.data
        
        #delete the lastnode
        q = deque([temp])
        while q:
            current = q.popleft()
            if current.left:
                if current.left == cur:
                    current.left = None
                    return
                else:
                    q.append(current.left)
                
            if current.right:
                if current.right == cur:
                    current.right = None
                    return
                else:
                    q.append(current.right)
        
    def traversal(self):
        
        def inorder(temp):
            if temp is None:
                return
            
            inorder(temp.left)
            print(temp.data, end = '->')
            inorder(temp.right)
        
        inorder(self.root)
        print("None")


bt = BinaryTree()
bt.insert(1)
# bt.insert(2)
# bt.insert(3)
bt.traversal()
bt.delete(1)
bt.traversal()
        
