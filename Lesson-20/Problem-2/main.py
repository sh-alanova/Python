n = int(input())
A = []
for i in range(n):
    name, grade = input().split()
    A.append((int(grade), name))
A.sort()
for elem in A:
    print(elem[0], elem[1])
    
