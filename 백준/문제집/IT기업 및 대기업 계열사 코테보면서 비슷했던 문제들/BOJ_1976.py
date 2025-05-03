import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, dest, visited):
    q = deque()
    q.append(start)

    moved = False
    while q:
        node = q.popleft()
        moved = False
        for next in data[node]:
            if next == dest and not visited[next]:
                return True
            if not visited[next]:
                q.append(next)
                moved = True
                visited[next] = True
        
    if not moved:
        return False


n = int(input())
m = int(input())

data = [[]*n for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    data[i].append(i)
    for j in range(len(temp)):
        if temp[j] == 1:
            data[i].append(j)
plan = list(map(int, input().split()))

answer = "YES"
for i in range(m-1):
    visited = [False]*n
    if not bfs(plan[i]-1, plan[i+1]-1, visited):
        answer = "NO"
        break
print(answer)