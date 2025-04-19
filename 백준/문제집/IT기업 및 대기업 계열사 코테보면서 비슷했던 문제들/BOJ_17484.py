import sys
input = sys.stdin.readline

dx = [-1, 0, 1]
DIRECTION = {0: "L", 1: "M", 2: "R"}

def dfs(x, y, val, prev_dir):
    if y == n - 1:
        results.append(val)
        return

    for d in range(3):  # L, M, R
        if d == prev_dir:
            continue 

        nx = x + dx[d]
        ny = y + 1

        if 0 <= nx < m:
            dfs(nx, ny, val + costs[ny][nx], d)

n, m = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(n)]
results = []
for i in range(m):
    dfs(i, 0, costs[0][i], -1)
print(min(results))