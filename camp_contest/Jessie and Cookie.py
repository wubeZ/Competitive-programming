import heapq


def cookies(k, A):
    count = 0
    heapq.heapify(A)
    
    while k > A[0]:
        if len(A) < 2:
            return -1
        x = heapq.heappop(A)
        y = heapq.heappop(A)
        heapq.heappush(A, x+(2*y))
        count += 1
        
    return count
