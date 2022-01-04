import math
AB = int(input())
BC = int(input())

AC = math.sqrt(pow(AB,2)+ pow(BC,2))

MC = AC/2
angC = math.asin(AB/AC)
BM = math.sqrt(pow(BC,2)+pow(MC,2)-(2*BC*MC*math.cos(angC)))
angT = math.asin((math.sin(angC)*MC)/BM)
angT = math.degrees(angT)
degree_sign = u'\N{DEGREE SIGN}'
print(str(round(angT))+ degree_sign)
