import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global depth

    visited[x][y] = True
    depth += 1
    for i in range(4):
        nx, ny = dx[i]+x, dy[i]+y

        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] != 0 and not visited[nx][ny]:
            dfs(nx, ny)

n = int(input())
data = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        depth = 0
        if not visited[i][j] and data[i][j] != 0:
            dfs(i, j)
            answer.append(depth)
print(len(answer))
for a in sorted(answer):
    print(a)