s = input()
sum = 0
k = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        k = k * 10 + int(s[i])  
    else:
        sum += k
        k = 0
sum += k
print(sum)
