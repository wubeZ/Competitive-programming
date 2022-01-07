from collections import OrderedDict
N = int(input())
answer = OrderedDict()
for i in range(N):
    item_name ,space, price = input().rpartition(" ")
    answer[item_name] = answer.get(item_name, 0) + int(price)

for i in answer:
    print(i,end = " ")
    print(answer[i])
