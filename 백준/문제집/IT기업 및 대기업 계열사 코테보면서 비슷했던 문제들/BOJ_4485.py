import sys, heapq
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijkstra():
    q=[]
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (data[0][0], 0, 0))
    distance[0][0] = data[0][0]
    #q가 비어있지 않다면
    while q:
        #가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(q)
        #현재 노드가 이미 처리됐다면 skip
        if distance[x][y] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드 확인

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + data[nx][ny]
                #현재 노드를 거치면 이동 거리가 더 짧은 경우

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

inf = sys.maxsize

t = 0
while True:
    n = int(input())
    t += 1
    if n == 0:
        break

    distance = [[inf] * n for _ in range(n)]
    data = [list(map(int, input().split())) for _ in range(n)]
    dijkstra()
    print(f"Problem {t}: {distance[n-1][n-1]}")