def BubbleSort(A, s): 
    ans = 0
    for j in range(len(A) - 1, 0, -1): 
        if s == 'ascending':
            for i in range(0, j): 
                if A[i] > A[i + 1]: 
                    A[i], A[i + 1] = A[i + 1], A[i]
        else:
            for i in range(0, j): 
                if A[i] < A[i + 1]: 
                    A[i], A[i + 1] = A[i + 1], A[i]                 
    return A

A = list(map(int, input().split()))
B = list(map(int, input().split()))
BubbleSort(A, 'ascending')
BubbleSort(B, 'descending')
ans = 0
for i in range(len(A)):
    ans += A[i] * B[i]
print(ans)
