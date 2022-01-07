from collections import deque
N = int(input())
command = []
d = deque()
for i in range(N):
    command = input().split()
    if command[0] =='append':
        d.append(int(command[1]))
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
num = list(d)
print(*num)
