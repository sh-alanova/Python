def Sort(A):
    count = [0] * 10 ** 5
    for elem in A:
        count[elem] += 1
    A[:] = []
    count.pop(0)   
    return count

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
B = Sort(B)
C = [0] * n
for i in range(n):
    C[i] = A[i] - B[i]
    if C[i] < 0:
        print('YES')
    else:
        print('NO')
