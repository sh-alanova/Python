n, m, k = map(int, input().split())
if (k - 2) * m < 2 * n  or k <= 2:
    print(0)
else:
    ans = (n + m + k - 1) // k
    print(ans)
