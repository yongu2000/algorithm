import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(q):
    queue = deque(q)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

queue = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])
        if box[i][j] == -1:
            box[i][j] = 1
bfs(queue)
zero_left = min(map(min, box))
if zero_left == 0:
    print(-1)
else:
    ans = max(map(max, box))
    print(ans-1)