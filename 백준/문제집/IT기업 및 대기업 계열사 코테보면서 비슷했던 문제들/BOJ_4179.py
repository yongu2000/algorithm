import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(start, fire_start):
    q = deque()
    for f in fire_start:
        f_sx, f_sy = f
        q.append((f_sx, f_sy, 1, "F"))
    s_x, s_y = start
    q.append((s_x, s_y, 1, "J"))

    while q:
        x, y, dist, obj = q.popleft()

        if obj == "J" and (x == 0 or y == 0 or x == r-1 or y == c-1):
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == ".":
                maze[nx][ny] = obj
                q.append((nx, ny, dist+1, obj))
        
    return "IMPOSSIBLE"

input = sys.stdin.readline

r, c = map(int, input().split())

maze = [list(input().strip()) for _ in range(r)]

start = ()
fire_start = []
for i in range(r):
    for j in range(c):
        if maze[i][j] == "J":
            start = (i, j)
        elif maze[i][j] == "F":
            fire_start.append((i, j))

print(bfs(start, fire_start))