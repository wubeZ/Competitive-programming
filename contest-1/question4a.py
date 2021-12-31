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
