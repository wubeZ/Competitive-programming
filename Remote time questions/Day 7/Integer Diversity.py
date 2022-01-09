if __name__ == '__main__':
    t = int(input())
    s = set()
    count = {}
    for i in range(t):
        n = int(input())
        integers = list(map(int, input().split()))
        s = set()
        for j in integers:
            if j not in s:
                s.add(j)
            else:
                s.add(-1*j)
        count[i] = len(s)
    for k in count.values():
        print(k)
