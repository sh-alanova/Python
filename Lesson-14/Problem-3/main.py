def gcd(a, b):
    global ans
    while a != 0 and b != 0:
        ans += a // b
        a = a % b
        a, b = b, a
    return ans
    
a = int(input())
b = int(input())
ans = 0
if max(a, b) % min(a, b) == 0:
    print(max(a, b) // min(a, b))
else:
    print(gcd(a, b))
    
            
