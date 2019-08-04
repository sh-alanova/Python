n = int(input())
min = n % 10
max = n % 10
while n > 0:
    digit = n % 10
    if digit < min:
        min = digit
    elif digit > max:
        max = digit
    n //= 10 
print(min, max)
