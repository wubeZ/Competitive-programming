S = input()
up = []
low = []
even = []
odd = []
for i in range(len(S)):
    if S[i].islower():
        low.append(S[i])
    elif S[i].isupper():
        up.append(S[i])
    elif S[i].isdigit():
        if int(S[i])%2 ==0:
            even.append(S[i])
        else:
            odd.append(S[i])
            
print("".join(sorted(low) + sorted(up) + sorted(odd) + sorted(even)))
