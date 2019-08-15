n = int(input())
k = int(input())
if n == 2:
    ans = 0
elif k <= n // 2:
    ans = n - k - 2
else:
    ans = k - 3
print(ans)
