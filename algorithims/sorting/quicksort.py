class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        
        if low == high:
            return
        
        pivot = self.partition(arr,low, high)
        self.quickSort(arr,low, pivot-1)
        self.quickSort(arr,pivot+1,high)
        
    
    def partition(self,arr,low,high):
        
        pivot = arr[high]
        b = low
        
        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[b] = arr[b], arr[i]
                b += 1
            else:
                #keep the taller person
                #will swap with shorter person
                b = b
        
        arr[high], arr[b] = arr[b], arr[high]
        return b
