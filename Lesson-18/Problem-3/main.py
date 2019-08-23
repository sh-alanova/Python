A = list(input().split())
stek = []
tmp = 0
for elem in A:
    if '0' <= elem <= '9':
        stek.append(elem)
    elif elem == '+':
        tmp = int(stek[-2]) + int(stek[-1])
        stek.pop()
        stek.pop()
        stek.append(tmp)
    elif elem == '*':
        tmp = int(stek[-2]) * int(stek[-1])
        stek.pop()
        stek.pop()        
        stek.append(tmp)
    elif elem == '-':
        tmp = int(stek[-2]) - int(stek[-1])
        stek.pop()
        stek.pop()        
        stek.append(tmp)
print(stek[-1])
