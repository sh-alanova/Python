a = int(input())
b = int(input())
IsPrime = [True] * (b + 1)
IsPrime[0] = False
IsPrime[1] = False
d = 2
while d * d <= b:
    if IsPrime[d]:
        for i in range(d * d, b + 1, d):
            IsPrime[i] = False
    d += 1
Primes = []
ans = 0
for i in range(a, b + 1):
    if IsPrime[i] == True:
        Primes.append(i)
print(len(Primes))
