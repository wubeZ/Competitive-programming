x , k = map(int,input().split())
P = input()
d = {}
d['x'] = x
y = eval(P,d)
if k == y:
    print("True")
else:
    print("False")
