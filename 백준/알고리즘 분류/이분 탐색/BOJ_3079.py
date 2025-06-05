import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

left = min(times)
right = max(times)*m

while left <= right:
    mid = (left + right) // 2

    total = 0
    for time in times:
        total += mid // time
    
    if total < m:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid 

print(ans)