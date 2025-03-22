import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))

ans = []
start = 0
end = n-1
MIN = sys.maxsize
while start < end:
    temp = nums[start] + nums[end]
    if abs(temp) < MIN:
        MIN = abs(temp)
        ans = [nums[start], nums[end]]
    elif temp < 0:
        start += 1
    else:
        end -= 1
print(*ans)