def gcd(a, b):
    if b == 0:
        return a
    else:
        while b != 0:
            a, b = b, a % b
        return a
      
a = int(input())
b = int(input())
n = int(input())
d = gcd(a, b)
sos_1 = sos_2 = 0
if a < n and b < n or n % d != 0:
    print('Impossible')
else:
    while sos_1 != n and sos_2 != n:
        if sos_1 == 0:
            print('>A')
            sos_1 = a
        elif sos_2 == b:
            print('B>')
            sos_2 =  0
        elif b - sos_2 >= sos_1:
            sos_2 += sos_1
            print('A>B')
            sos_1 = 0
        else:
            print('A>B')
            sos_1 -= (b - sos_2)
            sos_2 = b
            
            
