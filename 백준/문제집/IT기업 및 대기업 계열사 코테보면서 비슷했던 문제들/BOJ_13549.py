import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append([start, 0]) 

    while queue:
        position, time = queue.popleft()

        if position == k:
            return time
        a = position + 1
        b = position - 1
        c = position * 2
        if 0 <= c <= 100_000 and visited[c] < time:
            queue.append([c, time])    
            visited[c] = time
        if 0 <= a <= 100_000 and visited[a] < time+1:
            queue.append([a, time+1])        
            visited[a] = time+1
        if 0 <= b <= 100_000 and visited[b] < time+1:
            queue.append([b, time+1])    
            visited[b] = time+1
    return 

n, k = map(int, input().split())

visited = [0] * (100_001)

print(bfs(n))
