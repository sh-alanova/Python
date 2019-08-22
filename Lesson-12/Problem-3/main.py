def Hanoi(n, sum):
    if n == 1:
        sum += 1
    else:
        sum = Hanoi(n - 1, sum)
        sum += 1
        sum = Hanoi(n - 1, sum)
    return sum 
sum = 0
n = int(input())
print(Hanoi(n, sum))
