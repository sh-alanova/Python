def A(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, 1)
    else:
        return A(m - 1, (m, n - 1))

m = int(input())
n = int(input())
print(A(m, n))
