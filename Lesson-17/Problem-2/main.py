def SimpleCountingSort(A):
    B = [0] * 107
    x = min(A)
    for elem in A: 
        B[elem - x] += 1
    A[:] = []
    for j in range(x, x + 107):
        A += [j] * B[j - x]
    return A
n = int(input())
A = list(map(int, input().split()))
SimpleCountingSort(A)
for elem in A:
    print(elem, end = ' ')
