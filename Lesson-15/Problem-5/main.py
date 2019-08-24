def SumDel(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum += i + n // i 
        i += 1
    return sum

n = int(input())
for i in range(1, n + 1):
    j = SumDel(i)
    if i == SumDel(j) and i < j <= n:
        print(i, j)
