import sys
input = sys.stdin.readline

n = int(input())
U = list(int(input()) for _ in range(n))

xy = []
for i in U:
    for j in U:
        xy.append(i+j)
xy.sort()

answer = 0

for z in range(n):
    for k in range(z, n):
        left = 0
        right = len(xy) - 1

        target = U[k] - U[z]

        while left <= right:
            mid = (left + right) // 2

            if xy[mid] < target:
                left = mid + 1
            elif xy[mid] > target:
                right = mid - 1
            else: 
                answer = max(answer, U[k])
                break
print(answer)