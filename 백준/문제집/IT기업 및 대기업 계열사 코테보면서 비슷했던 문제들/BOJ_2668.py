import sys
input = sys.stdin.readline


def dfs(curr, start):
    visited[curr] = True
    next = data[curr]
    
    if not visited[next]:
        dfs(next, start)
    
    if visited[next] and next == start:
        answer.append(start)


n = int(input())
data = [0]

answer = []
for _ in range(n):
    data.append(int(input()))

for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i)

print(len(answer))
for a in answer:
    print(a)