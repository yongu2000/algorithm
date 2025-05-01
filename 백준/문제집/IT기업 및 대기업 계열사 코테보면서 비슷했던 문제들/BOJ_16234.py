import sys
from collections import deque
input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j, union):
    q = deque()
    visited[i][j] = True
    union.append([i, j, countries[i][j]])
    q.append([i, j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(countries[x][y] - countries[nx][ny]) <= r:
                q.append([nx, ny])
                visited[nx][ny] = True
                union.append([nx, ny, countries[nx][ny]])
    
n, l, r = map(int, input().split())

countries = [list(map(int, input().split())) for _ in range(n)]

answer = 0

while True:
    visited = [[False] * n for _ in range(n)]
    unions = []
    for i in range(n):
        for j in range(n):
            union = []
            if not visited[i][j]:
                bfs(i, j, union)
                unions.append(union)

    population = []

    for union in unions:
        sums = 0
        for u in union:
            sums += u[2]

        population.append(sums // len(union))

    if len(population) == n*n:
        break

    for idx, union in enumerate(unions):
        for u in union:
            x, y = u[0], u[1]
            countries[x][y] = population[idx]
    
    answer += 1
            
print(answer)