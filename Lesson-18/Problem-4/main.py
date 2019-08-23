n = int(input())
way1 = list(map(int, input().split()))
way2 = []
tup = []
k = 1
for i in range(n + 3):
    if len(tup) > 0 and tup[-1] == k:
        way2.append(tup.pop())
        k += 1
    elif len(way1) > 0 and way1[0] == k:
        way2.append(way1.pop(0))
        k += 1
    else:
        tup.append(way1.pop(0))
if len(way2) == n:
    print('YES')
else:
    print('NO')
        
 
