def Fib(n):
    if (n <= 2):
        return 1
    else:
        return Fib(n - 1) + Fib(n - 3)

n = int(input())
print(Fib(n))
