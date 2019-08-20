def Sort(A):
    count = [0] * 256
    for elem in A:
        count[ord(elem)] += 1
    A[:] = []
    for i in range(256):
        A += [chr(i)] * count[i]
    return A

A = list(input())
B = list(input())
Sort(A)
Sort(B)
if A == B:
    print('YES')
else:
    print('NO')
    
