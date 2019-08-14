A = list(map(int, input().split()))
max_count = 0
ans = 0
for elem in A:
    if A.count(elem) > max_count :
        max_count = A.count(elem)
        ans = elem
    elif A.count(elem) == max_count:
        ans = max(ans, elem)
print(ans)
