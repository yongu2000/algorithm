import sys
input = sys.stdin.readline
n, x = map(int, input().split())
visitors = list(map(int, input().split()))
sums = [0]
for i in range(n):
    sums.append(visitors[i] + sums[i])

max_visits = -sys.maxsize
visits = []
for i in range(x, n+1):
    visit = sums[i] - sums[i-x]
    visits.append(visit)
    max_visits = max(visit, max_visits)

if max_visits != 0:
    print(max_visits)
    print(visits.count(max_visits))
else:
    print("SAD")

