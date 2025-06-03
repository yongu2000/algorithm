import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

left = max(lectures)
right = sum(lectures)

while left <= right:
    mid = (left + right) // 2

    temp = 0
    count = 1
    for i in range(n):
        if temp + lectures[i] > mid:
            count += 1
            temp = 0
        temp += lectures[i]
    
    if count <= m:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)