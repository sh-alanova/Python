def Sort(A):
    count = [0] * 101
    for elem in A:
        count[elem] += 1
    A[:] = []
    for i in range(100):
        A += [i] * count[i]
    return A

Boot = list(map(int, input().split()))
People = list(map(int, input().split()))
Sort(Boot)
Sort(People)
i = j = ans = 0
while i < len(People) and j < len(Boot):
    if People[i] <= Boot[j]:
        i += 1
        j += 1
        ans += 1
    else:
        j += 1
print(ans)
    
