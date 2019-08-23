A = list(input())
stak = []
for elem in A:
    stak.append(elem)
    if len(stak) >= 2 and stak[-1] == stak[-2]:
        stak.pop()
        stak.pop()
for elem in stak:
    print(elem, end = '')
