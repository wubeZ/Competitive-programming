if __name__ == '__main__':
    print("enter a number: ", end=" ")
    H = int(input())
    for i in range(H+2):
        if i % 2 == 0:
            for j in range(3):
                print("##", end="  ")
            print()
        else:
            for k in range(2):
                print("  ", end="##")
            print()

