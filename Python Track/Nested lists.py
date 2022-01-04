if __name__ == '__main__':
    arr =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        
    arr.sort(key=lambda x:x[1])
    
    ans = []
    
    for i in range(len(arr)-2,-1,-1):
        
        if(arr[i][1] < arr[i+1][1]):
            ans.append(arr[i][0])
            i -= 1
            while(arr[i][1] == arr[i+1][1]):
                ans.append(arr[i][0])
                i -=1
                
    ans.sort()
    for std in ans:
        print(std)
     
