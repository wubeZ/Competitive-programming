if __name__ == '__main__':
    N = int(input("Enter a number: "))
    for i in range(2):
        for j in range(N):
            for k in range(N-1):
                print("#", end=" ")
            print(" ", end=" ")
        print()
