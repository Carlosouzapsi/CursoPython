from math import fabs

a,b,s = input().split(" ")

a = int(a)
b = int(b)
s = int(s)

maiorAB = (a + b + fabs(a - b))/2
maiorBC = (maiorAB + s + fabs(maiorAB - s)) / 2
print(f'{int(maiorBC)} eh o maior')




