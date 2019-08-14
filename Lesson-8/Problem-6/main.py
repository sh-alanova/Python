A = list(map(int, input().split()))
B = []
for elem in A:
    if elem not in B:
        B.append(elem)
print(len(B))
