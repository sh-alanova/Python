n = 10 ** 5
IsPrime = [True] * (n + 1)
IsPrime[0] = False
IsPrime[1] = False
d = 2
while d * d <= n:
    if IsPrime[d]:
        for i in range(d * d, n + 1, d):
            IsPrime[i] = False
    d += 1
i = n
while i > 0:
    if IsPrime[i] == True and str(i) == str(i)[::-1]:
        print(i)
        break
    i -= 1
    
