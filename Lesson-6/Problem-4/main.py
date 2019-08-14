n = int(input())
min_dig = max_dig = n % 10
while n > 0:
    digit = n % 10
    if digit < min_dig:
        min_dig = digit
    elif digit > max_dig:
        max_dig = digit
    n //= 10 
print(min_dig, max_dig)
