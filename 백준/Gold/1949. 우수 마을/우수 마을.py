import sys

sys.setrecursionlimit(20000)

def dfs(node):
    visited[node] = True

    dp[node][0] = 0
    dp[node][1] = people[node]
    
    for next in data[node]:
        if not visited[next]:
            dfs(next)
            dp[node][1] += dp[next][0]
            dp[node][0] += max(dp[next][0], dp[next][1])

n = int(input())
people = [0] + list(map(int, input().split()))
data = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)

dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)
dfs(1)
print(max(dp[1][0], dp[1][1]))
