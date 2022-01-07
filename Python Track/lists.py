if __name__ == '__main__':
    N = int(input())
    ans = []
    for i in range(N):
        
        commands =  input().split() 
        if "insert" == commands[0]:
            ans.insert(int(commands[1]),int(commands[2]))
            
        elif "print" ==commands[0]:
            print(ans)
        elif "remove" == commands[0]:
            ans.remove(int(commands[1])) 
        elif "append" == commands[0]:
            ans.append(int(commands[1]))
        elif "sort" == commands[0]:
            ans.sort()
        elif "pop" == commands[0]:
            ans.pop()
        elif "reverse" == commands[0]:
            ans.reverse()
            
            
        
                   
        
