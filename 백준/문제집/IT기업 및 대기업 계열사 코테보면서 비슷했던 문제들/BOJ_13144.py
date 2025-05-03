import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
visited = [False]*(n+1)

left, right = 0, 0
answer = 0
while left < n and right < n:
    if not visited[nums[right]]:
        visited[nums[right]] = True
        right += 1
        answer += right - left
    else:
        visited[nums[left]] = False
        left += 1

print(answer)