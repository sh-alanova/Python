s = input()
ans = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        ans += 1
print(ans)
