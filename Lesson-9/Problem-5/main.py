f = open('input.txt')
A = f.read().split()
sum = 0
for i in range(len(A)):
    sum += int(A[i]) 
g = open('output.txt', 'w')
g.write(str(sum))
f.close()
g.close()
