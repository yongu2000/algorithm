import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start):
    if visited[start]:
        return

    visited[start] = 1
    for e in computers[start]:
        dfs(e)

v = int(input())
e = int(input())
computers = [[] for _ in range(v+1)]
visited = [0] * (v+1)
for _ in range(e):
    v1, v2 = map(int, input().split())
    computers[v1].append(v2)
    computers[v2].append(v1)

dfs(1)
print(sum(visited)-1)