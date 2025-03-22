import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 0
end = k

while start <= end:
    mid = (start + end) // 2
    index = 0

    for i in range(1, n+1):
        index += min(mid//i, n)

    if index >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1


print(answer)