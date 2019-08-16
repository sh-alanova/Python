def Hanoi(n, st, fn):
    tmp = 6 - st - fn
    if n == 1:
        if fn == st + 1 or fn == (st + 2) % 3:
            print(n, st, fn)
        else :
            print(n, st, tmp)
            print(n, tmp, fn)
    else:
        if fn == st + 1 or fn == (st + 2) % 3:
            Hanoi(n - 1, st, tmp)
            print(n, st, fn)
            Hanoi(n - 1, tmp, fn)
        else:
            Hanoi(n - 1, st, fn)
            print(n, st, tmp)
            Hanoi(n - 1, fn, st)   
            print(n, tmp, fn);
            Hanoi(n - 1, st, fn)
            
n = int(input())
Hanoi(n, 1, 3)
