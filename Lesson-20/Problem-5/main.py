n = int(input())
A = list(map(int, input().split()))
B = [0] * n
for i in range(n):
    B[i] = (A[i], i)
B.sort(reverse = True)
sum = 0
for i in range(n):
    sum += B[i][0] * (i + 1)
print(sum)
for i in range(n):
    print(B[i][1] + 1, end = ' ')
   

