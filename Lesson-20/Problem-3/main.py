n = int(input())
A = list(map(int, input().split()))
A.sort()
i = len(A) - 3
while i >= 0:
    A.pop(i)
    i -= 3
sum = 0
for elem in A:
    sum += elem 
print(sum)
