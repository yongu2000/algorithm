import sys
input = sys.stdin.readline

n, m = map(int, input().split())
plans = [int(input()) for _ in range(n)]

left = min(plans)
right = sum(plans)


while left <= right:
    mid = (left + right) // 2

    count = 1
    temp = mid
    for p in plans:
        if temp - p < 0:
            count += 1
            temp = mid
        temp -= p
    
    if count > m or mid < max(plans):
        left = mid + 1
    else:
        right = mid - 1
        ans = mid

print(ans)