import sys
input=sys.stdin.readline
from collections import deque

deck=deque()
n=int(input())
for _ in range(n):
    op=input().rstrip()
    if op=='pop_front':
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif op=='pop_back':
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif op=='size':
        print(len(deck))
    elif op=='empty':
        if deck:
            print(0)
        else:
            print(1)
    elif op=='front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif op=='back':
        if deck:
            print(deck[-1])
        else:
            print(-1)
    else:
        ops=op.split()
        if ops[0]=='push_front':
            deck.appendleft(int(ops[1]))
        else:
            deck.append(int(ops[1]))
