def Pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * Pow(a, n - 1) % 1000
    else:
        return Pow(a, n // 2) ** 2 % 1000

a = int(input())
n = int(input())
print(Pow(a, n) % 1000)
