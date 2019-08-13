def SumDel(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i 
    return sum

n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == SumDel(j) and j == SumDel(i) and i < j:
            print(i, j)
    
