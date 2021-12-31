if __name__ == '__main__':
    H = int(input())

    for i in range(1,H+1):
        for j in range(H - i):
            print(" ", end =" ")
        for k in range(1,i+1):
            print(k, end=" ")
        for l in range(1,i):
            print(i-l,end =" ")
        print()
        num = 1
    for i in range(1,H):
        for j in range(i):
            print(" ", end =" ")
        for k in range(H-i,1,-1):
            print(num, end=" ")
            num+=1
        for l in range(H-i,0,-1):
            print(l,end =" ")
        num =1
        print()