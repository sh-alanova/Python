s = input()
sum = 0
k = 0
for c in s:
    if '0' <= c <= '9':
        k = k * 10 + int(c)  
    else:
        sum += k
        k = 0
sum += k
print(sum)
