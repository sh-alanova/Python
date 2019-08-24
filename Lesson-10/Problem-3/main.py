f = open('input.txt')
g = open('output.txt', 'w')
A = f.read().split()
D = {}
for elem in A:
    if elem not in D:
        D[elem] = 0
    D[elem] += 1
max_value = 0
max_key = ''
for key in D:
    if max_value < D[key] or (max_value == D[key] and max_key > key):
        max_value = D[key]
        max_key = key
g.write(max_key)
f.close()
g.close()     
