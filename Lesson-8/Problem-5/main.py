s = input().split()
A = list(map(int, s))
count = 0
for i in range(0, len(A)):
    if A[i] > 0:
        count += 1
print(count)
