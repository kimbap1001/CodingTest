from collections import deque

def bfs(n:int, computers:list[list[int]], visited:list[bool], start:int)->None:
    queue=deque([start])
    visited[start]=True

    while queue:
        computer=queue.popleft()
        for index, isConnected in enumerate(computers[computer]):
            if isConnected==1 and not visited[index]:
                visited[index]=True
                queue.append(index)

def solution(n, computers):
    visited=[False]*n
    total_nets=0
    for index in range(n):
        if not visited[index]:
            total_nets+=1
            bfs(n, computers, visited, index)

    return total_nets