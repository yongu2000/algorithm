import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cookies = list(map(int, input().split()))

left = 1
right = max(cookies)
ans = 0

while left <= right:
    mid = (left + right) // 2

    count = 0
    for cookie in cookies:
        count += cookie // mid

    if count >= n:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
    
print(ans)