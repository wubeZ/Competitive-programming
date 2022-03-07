import heapq

def main():
    heap = []
    delset = set()
    n = int(input())
    
    for i in range(n):
        
        x = input().rstrip().split()
        
        if x[0] == '1':
            heapq.heappush(heap, int(x[1]))
            delset.add(int(x[1]))
        
        elif x[0] == '2':
            delset.discard(int(x[1]))
            
        elif x[0] == '3':
            while heap[0] not in delset:
                heapq.heappop(heap)
                
            print(heap[0])
            
            
main()