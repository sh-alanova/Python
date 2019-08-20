def Bublesort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                                
f = open('input.txt')
g = open('output.txt', 'w')
A = f.read().split()
D = {}
for elem in A:
    D[elem] = 0
for elem in A:
    D[elem] += 1
max_value = 0
max_key = ''
for key in D:
    if max_value < D[key]:
        max_value = D[key]
        max_key = key
if max_value == 1:
    Bublesort(A)
    g.write(A[0])
else:
    g.write(max_key)
f.close()
g.close()     
