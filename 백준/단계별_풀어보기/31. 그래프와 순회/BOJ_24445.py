import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global depth
    queue = deque()
    queue.append(start)
    visited[start] = depth
    depth += 1
    while queue:
        edge = queue.popleft()
        for e in sorted(graph[edge], reverse=True):
            if visited[e] == 0:
                visited[e] = depth
                depth += 1 
                queue.append(e)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
depth = 1

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

bfs(r)

for i in range(1, n+1):
    print(visited[i])
