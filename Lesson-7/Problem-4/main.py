s = input()
sum = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        sum += int(s[i])
print(sum)
