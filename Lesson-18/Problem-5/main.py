A = list(map(int, input().split()))
stak = []
ans = 0
i = 0
while i < len(A):
    stak.append(A[i])
    if len(stak) >= 3 and stak[-1] == stak[-2] == stak[-3]:
        tmp = stak[-1]
        ans += 2
        stak.pop()
        stak.pop()
        stak.pop()
        while i < len(A) and A[i] == tmp:
            ans += 1
            i += 1
    else:
        i += 1
print(ans)
