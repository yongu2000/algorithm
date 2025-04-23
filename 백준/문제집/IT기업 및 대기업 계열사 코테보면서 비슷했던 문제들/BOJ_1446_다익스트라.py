import sys, heapq
input = sys.stdin.readline

n, d = map(int, input().split())
inf = sys.maxsize

data = [[] for _ in range(d+1)]
distance = [inf] * (d+1)

for i in range(d):
    data[i].append((i+1, 1))

for _ in range(n):
    u, v, w = map(int, input().split())    # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치 
    if v <= d:
        data[u].append((v, w))             # 도착, 거리

q = []
heapq.heappush(q, (0,0)) # (위치, 지나온 거리)
distance[0] = 0

while q:
    w1, u = heapq.heappop(q) # (위치, 지나온 거리) *가장 적은 위치

    for v, w2 in data[u]: # 그 위치에서 가능한 모든 경로 중에서
        cost = distance[u] + w2 # 그 위치의 현재 지나온 거리 + 가능한 경로의 가중치
        if distance[v] > cost: # 그게 목표 지점의 가중치보다 낮은 경우, 이 경로를 선택하는걸로 변경
            distance[v] = cost
            heapq.heappush(q, (cost, v))
print(distance[d])



# DP 풀이

# import sys

# n, d = map(int, sys.stdin.readline().split())

# dp = [i for i in range(d+1)]

# shortcuts = []

# for _ in range(n):
#     start, dest, length = map(int, sys.stdin.readline().split())
#     if dest - start > length:
#         shortcuts.append((start, dest, length))
# shortcuts.sort()

# for start, dest, length in shortcuts:
#     for i in range(1, d+1):
#         if dest == i:
#             dp[i] = min(dp[i], dp[start]+length)
#         else:
#             dp[i] = min(dp[i], dp[i-1]+1)
# print(dp[d])