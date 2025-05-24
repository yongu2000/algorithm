import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
inf = sys.maxsize

graph = [[] for _ in range(n+1)]


for _ in range(m):
    start, end, t = map(int, input().split())
    graph[start].append([end, t])


def dijkstra(start):
    q=[]
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    #q가 비어있지 않다면
    while q:
        #가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, node = heapq.heappop(q)
        #현재 노드가 이미 처리됐다면 skip
        if distance[node] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드 확인
        for dest, weight in graph[node]:
            cost = dist + weight
            #현재 노드를 거치면 이동 거리가 더 짧은 경우
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(q, (cost, dest))

distance = [inf] * (n+1)
return_home = [-1] * (n+1)
dijkstra(x)


answer = [0] * (n+1)
for i in range(n+1):
    return_home[i] = distance[i]


for i in range(1, n+1):
    if i == x:
        continue
    distance = [inf] * (n+1)
    dijkstra(i)

    answer[i] = distance[x] + return_home[i]

print(max(answer))