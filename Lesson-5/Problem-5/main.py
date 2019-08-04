a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 10 == i // 1000 and i // 10 % 10 == i // 100 % 10:
        print(i)
    
