import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, data):
    data[x][y] = 0
    for i in range(4):
        nx, ny = dx[i]+x, dy[i]+y

        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 0:
            dfs(nx, ny, data)
    return data

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if field[i][j]:
                dfs(i, j, field)
                answer += 1
    print(answer)