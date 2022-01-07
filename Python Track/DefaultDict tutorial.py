from collections import defaultdict
n,m = map(int,input().split())
A = defaultdict(list)
for i in range(1,n+1):
   A[input()].append(i)

for i in range(1,m+1):
    B = input()
    if len(A[B]) > 0:
        print(" ".join(str(j) for j in A[B]))
    else:
        print(-1)
