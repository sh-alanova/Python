n = int(input())
k = int(input())
if(1 <= k <= n <= 50) and n % 2 == 0:
    if k == n / 2:
        print(0)
    elif k < n / 2:
        t = n // 2 - k
        print(t)
    else:
        t =  n // 2 - (n - k + 1)
        print(t)
