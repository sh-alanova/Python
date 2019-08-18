def BubbleSort(A): 
    ans = 0
    for j in range(len(A) - 1, 0, -1): 
        for i in range(0, j): 
            if A[i] > A[i + 1]: 
                A[i], A[i + 1] = A[i + 1], A[i]
    return A

def UnbubbleSort(B): 
    ans = 0
    for j in range(len(B) - 1, 0, -1): 
        for i in range(0, j): 
            if B[i] < B[i + 1]: 
                B[i], B[i + 1] = B[i + 1], B[i]
    return B

A = list(map(int, input().split()))
B = list(map(int, input().split()))
BubbleSort(A)
UnbubbleSort(B)
ans = 0
for i in range(len(A)):
    ans += A[i] * B[i]
print(ans)
