
from collections import deque

directions = [1, -1]

def dfs(n:int, numbers:list, target:int)->int:
    stack = deque([(0,numbers[0]), (0,-numbers[0])])
    result=0

    while stack:
        depth, sum = stack.pop()
        if depth<n-1:
            for dx in directions:
                stack.append((depth+1, sum+dx*numbers[depth+1]))
        else:
            if sum == target:
                result+=1

    return result

def solution(numbers, target):
    return dfs(len(numbers), numbers, target)