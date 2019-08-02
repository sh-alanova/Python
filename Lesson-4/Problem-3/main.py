a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = c - a
f = d - b
if (f < 0):
    f = 100 - b + d
    e = e - 1
print(e, f)
