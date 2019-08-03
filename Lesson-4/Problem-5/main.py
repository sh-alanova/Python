a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (c == 0 and d == 0) or a == 0 or (- b // a) == (- d // c):
    print('NO')
elif a == 0 and b == 0:
    print('INF')
elif(b % a == 0):
    print(- b // a)
else:
    print('NO')
