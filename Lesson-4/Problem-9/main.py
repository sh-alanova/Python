n = int(input())
m = int(input())
k = int(input())
count = k // n
ans = 0
while m > 0:
    m -= count
    ans += 1
print(ans)
