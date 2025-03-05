import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append([start, 0])
    visited[start] = True

    while queue:
        node, parent = queue.popleft()
        visited[node] = True
        for n in data[node]:
            if n != parent and visited[n] == False:
                queue.append([n, node])
            if n != parent and visited[n] == True:
                return False
    return True

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    data = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    for _ in range(e):
        v1, v2 = map(int, input().split())
        data[v1].append(v2)
        data[v2].append(v1)

    ans = "NO"
    for i in range(1, v+1):
        if len(data[i]) == 2 and bfs(i):
            ans = "YES"
            break

    print(ans)