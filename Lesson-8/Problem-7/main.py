s = input().split()
A = list(map(int, s))
min_el = None
for elem in A:
    if (min_el is None) and elem > 0:
        min_el = elem
    elif (min_el is not None) and min_el > elem and elem > 0:
        min_el = elem
print(min_el)
