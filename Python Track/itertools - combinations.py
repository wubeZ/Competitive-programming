from itertools import combinations
S,k = map(str,input().split())
k = int(k)
S = sorted(S)

for i in range(1,k+1):
    for j in combinations(S,i):
        print("".join(j))
