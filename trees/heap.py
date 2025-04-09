class MinHeap:
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.arr = [0] * self.capacity
    
        
    def extract_min(self):
        if self.size == 0:
            return -1
        
        root = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.heapify(0)
        return root
        
    #top down (top to down)
    #called while extract min
    def heapify(self, i):
        smallest = i
        left = self.left(i)
        right = self.right(i)
        
        if left < self.size and self.arr[left] < self.arr[smallest]:
            smallest = left
        if right < self.size and self.arr[right] < self.arr[smallest]:
            smallest = right
        
        if smallest != i:
            self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
            self.heapify(smallest)
    

    def insert(self, val):
        if self.size == self.capacity:
            print("Heap is full!")
            return
        
        k = self.size
        #insert at end
        self.arr[k] = val
        self.size += 1
        
        while k != 0 and self.arr[k] < self.arr[self.parent(k)]:
            self.arr[k], self.arr[self.parent(k)] = self.arr[self.parent(k)], self.arr[k]
            k = self.parent(k)
    
    def get_min(self):
        return self.arr[0] if self.size > 0 else -1


minheap = MinHeap(5)
minheap.insert(5)
minheap.insert(4)
minheap.insert(3)
print(minheap.get_min())        # Output: 3

print(minheap.extract_min())    # Output: 3
print(minheap.get_min())        # Output: 4

