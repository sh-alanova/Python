def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
    

k = int(input())
t = 2
i = 0
while i != k:
    if IsPrime(t):
        i += 1
    t += 1
print(t - 1)
    
