n,m  =  map(int,input().split())

arr = list(map(int,input().split()))
A=  set(map(int,input().split()))
B =  set(map(int,input().split()))

hap =0
for i in range(len(arr)):
    if arr[i] in A:
        hap +=1
    if arr[i]  in B:
        hap-=1
print(hap)
