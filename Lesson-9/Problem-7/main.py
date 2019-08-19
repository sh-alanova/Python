f = open('input.txt')
A = f.read().split()
A = ' '.join(A)
sum = 0
minus = 0
number = 0
for i in range(len(A)):
    if '0' <= A[i] <= '9': 
        if i > 0 and A[i - 1] == '-':
            minus = 1
        number = 10 * number + int(A[i]) 
    else:
        if minus == 1:
            number = -number
            minus = 0
        sum += number
        number = 0 
if minus == 1:
    number = -number
sum += number     
g = open('output.txt', 'w')
g.write(str(sum))
f.close()
g.close()

