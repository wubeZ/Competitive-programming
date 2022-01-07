from itertools import product
n = set(map(int,input().split()))
m = set(map(int,input().split()))
o = list(product(n,m))
for i in o:
    print(i,end=" ")
