import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start) 
    visited[start] = 0

    while queue:
        position = queue.popleft()

        if position == k:
            return visited[position]
        
        a = position - 1
        b = position + 1
        c = position * 2

        if 0 <= c <= 100_000 and visited[c] == -1:
            queue.appendleft(c)    
            visited[c] = visited[position]
        if 0 <= a <= 100_000 and visited[a] == -1:
            queue.append(a)        
            visited[a] = visited[position] + 1
        if 0 <= b <= 100_000 and visited[b] == -1:
            queue.append(b)    
            visited[b] = visited[position] + 1

n, k = map(int, input().split())
visited = [-1] * 100_001

print(bfs(n))
