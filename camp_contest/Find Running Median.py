import heapq


def runningMedian(a):    
    left = []
    right = []
    ans = []
    
    for val in a:
        if len(left) > len(right):
            t = heapq.heappushpop(left,-1*val)
            heapq.heappush(right,-1*t)

        else:
            t = heapq.heappushpop(right,val)
            heapq.heappush(left,-1*t)
            
        ans.append(findMedian(left,right))
    
    return ans    

def findMedian(left,right):
        if len(left) == len(right):
            return (-left[0] + right[0])/2
        else:
            return -1.0 * left[0]
