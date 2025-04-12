import sys
input = sys.stdin.readline

def lighted(mid):
    covered = 0
    for x in X:
        if x - mid > covered:
            return False
        covered = max(covered, x + mid)
        if covered >= n:
            return True
    return covered >= n

n = int(input())
m = int(input())
X = list(map(int, input().split()))

left = 1
right = n

while left <= right:
    mid = (left + right) // 2

    if lighted(mid):
        right = mid - 1
    else:
        left = mid + 1

print(right+1)