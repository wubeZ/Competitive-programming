T = int(input())
for i in range(T):
    a,b = input().split()
    try:
        print(int(a)//int(b))  
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)