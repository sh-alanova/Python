from collections import deque

n = int(input())
queue1 = deque()
queue2 = deque()
for i in range(n):
    s = input().split()
    if s[0] == '-':
        print(queue1.popleft())
    elif s[0] == '+':
        queue2.append(s[1])
    else:
        queue2.appendleft(s[-1])
    if len(queue2) > len(queue1):
        tmp = queue2.popleft()
        queue1.append(tmp)    

    
