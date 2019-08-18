def Bublesort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
def Pop(A, x):
    k = 0
    while A[k] < x:
        k += 1
    while k > 0:
        A.pop(0)
        k -= 1
    return A

size = int(input())
A = list(map(int, input().split()))
Bublesort(A)
if A[-1] < size:
    print(0)
else:
    Pop(A, size)
    ans = 1
    min_size = A[0]
    for i in range(1, len(A)):
        if A[i]  >= min_size + 3:
            ans += 1
            min_size = A[i]
    print(ans)
      
