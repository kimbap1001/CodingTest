import sys
input=sys.stdin.readline
from collections import deque

queue=deque()
n=int(input())
for _ in range(n):
    op=input().rstrip()
    if op=='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif op=='size':
        print(len(queue))
    elif op=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif op=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif op=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        ops=op.split()
        queue.append(int(ops[1]))
