s = input()
sum = 0
for c in s:
    if '0' <= c <= '9':
        sum += int(c)
print(sum)
