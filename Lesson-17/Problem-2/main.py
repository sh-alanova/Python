def SimpleCountingSort(A):
    B = [0] * 107
    x = min(A)
    for i in range(x, x + 107): 
        B[i - x] = A.count(i)
    A[:] = []
    for j in range(x, x + 107):
        A += [j] * B[j - x]
    return A
n = int(input())
A = list(map(int, input().split()))
SimpleCountingSort(A)
for elem in A:
    print(elem, end = ' ')
