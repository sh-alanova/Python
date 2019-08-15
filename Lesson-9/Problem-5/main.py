f = open('input.txt')
A = f.read().split()
sum = 0
for elem in A:
    sum += int(elem) 
g = open('output.txt', 'w')
g.write(str(sum))
f.close()
g.close()
