A = list(input())
stek = []
for elem in A:
    if elem == '(' or elem == '[' or elem == '{':
        stek.append(elem)
    else:
        if stek == []:
            print('NO')
            break
        elif (stek[-1] == '(' and elem == ')') or (stek[-1] == '[' and elem == ']') or (stek[-1] == '{' and elem == '}'):
            stek.pop()         
        else:
            print('NO')
            break
else:
    if stek != []:
        print('NO')
    else:
        print('YES')
        
