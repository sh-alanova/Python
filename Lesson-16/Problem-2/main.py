def BubbleSort(A): 
    ans = 0
    for j in range(len(A) - 1, 0, -1): 
        for i in range(0, j): 
            if A[i] > A[i + 1]: 
                A[i], A[i + 1] = A[i + 1], A[i]
    med = len(A) // 2 
    return A[med]
A = list(map(int, input().split()))
print (BubbleSort(A))
