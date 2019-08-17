a = int(input())
b = int(input())
ans = 0
while b != 0:
    ans += a // b
    a, b = b, a % b
print(ans)
