s = input().split()
A = list(map(int, s))
min_el = A[0]
for elem in A:
    if min_el > elem and elem > 0:
        min_el = elem
print(min_el)
