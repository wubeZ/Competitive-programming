# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

ans= set()
for i in range(N):
    ans.add(input())
print(len(ans))
