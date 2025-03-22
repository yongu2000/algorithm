import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))
costs.pop()
min_cost = sys.maxsize
answer = 0

for i in range(len(roads)):    
    if costs[i] <= min_cost:
        min_cost = costs[i]
    answer += roads[i] * min_cost

print(answer)
