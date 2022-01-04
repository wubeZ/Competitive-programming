def ourprint(nums,nums2):
    lisnums = []
    for i in nums:
        lisnums.append(i)
    for j in nums2:
        lisnums.append(j)
    lisnums.sort()
    
    for i in lisnums:
        print(i)
        
        
M = int(input())
J = set(map(int,input().split()))

N = int(input())
J2 = set(map(int,input().split()))
ourprint(J2.difference(J),J.difference(J2))
