def gcd(a, b):
    if a > 0 and b > 0:
        while a != 0 and b != 0:
            a = a % b
            a, b = b, a
        return max(a, b)
    else:
        return 0
    
    
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0: 
    print(abs((abs(x2) - abs(x1))) + abs((abs(y2) - abs(y1))) - gcd(abs((abs(x2) - abs(x1))), abs((abs(x2) - abs(x1)))))
else:
    print(abs(x2 - x1) + abs(y2 - y1) - gcd(abs(x2 - x1), abs(y2 - y1)))
    
            
