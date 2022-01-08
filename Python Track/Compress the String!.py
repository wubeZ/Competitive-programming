import itertools 
S = input()
group = itertools.groupby(map(int,list(S)))
for i,j in group:
    print(tuple([len(list(j)), i]) ,end = " ")