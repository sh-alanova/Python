n, m, k = map(int, input().split())
big = m / 2
little = n  / (k - 2)
if little > big or k <= 2:
    print(0)
else:
    ans = (n + m + k - 1) // k
    print(ans)
