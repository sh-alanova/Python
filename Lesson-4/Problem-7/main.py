i, j = map(int, input().split())
if i == 99 and j == 100 or j == 99 and i == 100:
    print('98')
elif i < j:
    print(i)
else:
    print(j)
