n = int(input())
min_dig = max_dig = n % 10
while n > 0:
    digit = n % 10
    min_dig = min(digit, min_dig)
    max_dig = max(digit, max_dig)
    n //= 10 
print(min_dig, max_dig)
