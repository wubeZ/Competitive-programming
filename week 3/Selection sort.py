class Solution: 
    def select(self, arr, i):
        arr = arr[:i]
        return arr
    
    def selectionSort(self, arr,n):
        for i in range(n):
            index = i
            for j in range(i+1,n):
                if arr[index] > arr[j]:
                    index = j
            arr[i],arr[index] = arr[index],arr[i]
        return arr
                    