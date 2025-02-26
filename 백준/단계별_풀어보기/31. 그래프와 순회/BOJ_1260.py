import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start):
    if visited[start]:
        return
    visited[start] = 1
    dfs_res.append(start)
    for node in sorted(graph[start]):
        dfs(node)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        node = queue.popleft()
        bfs_res.append(node)
        for n in sorted(graph[node]):
            if not visited[n]:
                visited[n] = 1
                queue.append(n)

v, e, r = map(int, input().split())
graph = [[] for _ in range(v+1)]
dfs_res = []
bfs_res = []
for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (v+1)
dfs(r)
print(*dfs_res)
visited = [0] * (v+1)
bfs(r)
print(*bfs_res)
