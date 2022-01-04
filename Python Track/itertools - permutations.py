from itertools import permutations
S , k = map(str,input().split())
k = int(k)

o = list(permutations(S,k))
o.sort()
for i in o:
    print("".join(i))
