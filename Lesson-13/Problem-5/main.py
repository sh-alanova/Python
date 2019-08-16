def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
    
n = int(input())
i = 2
while (not (IsPrime(i) and  IsPrime(n - i))):
    i += 1  
print(i, n - i)
            
