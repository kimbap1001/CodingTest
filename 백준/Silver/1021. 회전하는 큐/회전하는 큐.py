import sys
input=sys.stdin.readline
from collections import deque

n, _ = map(int, input().split())
queue=deque([i+1 for i in range(n)])
targets=list(map(int, input().split()))
result=0
for target in targets:
    idx=queue.index(target)
    if abs(len(queue)-idx)<abs(-idx):
        result+=abs(len(queue)-idx)
        queue.rotate(len(queue)-idx)
        queue.popleft()
    else:
        result+=idx
        queue.rotate(-idx)
        queue.popleft()
print(result)