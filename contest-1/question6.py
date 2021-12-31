if __name__ == '__main__':
    ans = []
    arr = list(map(int, input().split()))
    for i in arr:
        if int(i) != 0:
            ans.append(i)
    num = len(arr) - len(ans)
    for j in range(num):
        ans.append(0)
    print(ans)

