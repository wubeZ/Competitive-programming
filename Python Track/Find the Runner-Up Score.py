if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    i = len(arr)-1
    for j in range(i,-1,-1):
        if(arr[j]!=arr[j-1]):
            print(arr[j-1])
            break

    
