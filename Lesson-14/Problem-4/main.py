def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = abs(x2 - x1)
b = abs(y2 - y1)
if a == 0 or b == 0:
    print(0)
else:
    ans = a + b - gcd(a, b)
    print(ans)
    
