import sys
from collections import deque
input=sys.stdin.readline

def solve(n:int, k:int)->list:
    people=deque([i+1 for i in range(n)])
    result=[]
    for _ in range(n):
        people.rotate(-(k-1))
        result.append(people.popleft())
    return result

def main()->None:
    n, k=map(int, input().split())
    result=solve(n,k)
    print('<' + ', '.join(map(str, result)) + '>')


main()