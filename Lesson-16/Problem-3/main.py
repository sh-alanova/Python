def BubbleSort(A): 
    ans = 0
    for j in range(len(A) - 1, 0, -1): 
        for i in range(0, j): 
            if A[i] > A[i + 1]: 
                A[i], A[i + 1] = A[i + 1], A[i]
    return A
S, N = map(int, input().split())
A = []
A_summa = 0
for i in range(N):
    A.append(int(input()))
    N -= 1
    A_summa += A[i]
BubbleSort(A)
sum = i = ans = 0
if A_summa > S:
    while sum <= S:
            sum += A[i]
            i += 1
            ans += 1
else:
    ans = len(A) + 1
print(ans - 1)
