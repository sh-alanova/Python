s = input().split()
A = list(map(int, s))
B = []
for i in range(0, len(A)):
    if A[i] > 0:
        B.append(A[i])
min = B[0]
for i in range(0, len(B)):
        if min > B[i]:
            min = B[i]
print(min)
