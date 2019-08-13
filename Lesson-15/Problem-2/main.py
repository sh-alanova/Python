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
Palindroms = []
for i in range(0, n + 1):
    if IsPrime[i] == True and str(i) == str(i)[::-1]:
        Palindroms.append(i)

print(Palindroms[-1])