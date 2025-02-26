import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start):
    global depth
    if visited[start] != 0:
        return

    visited[start] = depth
    depth += 1
    for e in sorted(graph[start]):
        dfs(e)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
depth = 1

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(r)

for i in range(1, n+1):
    print(visited[i])
