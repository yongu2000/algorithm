import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[-1] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[x][y] > graph[nx][ny]:
            visited[x][y] += dfs(nx, ny)

    return visited[x][y]

print(dfs(0, 0))