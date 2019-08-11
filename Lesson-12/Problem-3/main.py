def Hanoi(n):
    global sum
    if n == 1:
        sum +=1
    else:
        Hanoi(n - 1)
        sum += 1
        Hanoi(n - 1)
    return sum 
sum = 0
n = int(input())
print(Hanoi(n))
