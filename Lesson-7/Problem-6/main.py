k = int(input())
size = 0
s = '1'
t = ''
while k > 1:
    digit = s[0]
    size = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            size += 1
        else:
            t += str(size) + str(digit)
            size = 1
            digit = s[i]
    t += str(size) + str(digit)
    s = t
    t = ''
    k -= 1
print(s)
        
