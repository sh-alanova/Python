sum = 0
for i in range(1, 99):
    term = 1;
    for j in range(i, i + 3):
        term *= j;
    sum += term
print(sum)
    
