import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

stack = []
data = {}
ans = [-1] * n

for a in A:
    if a in data:
        data[a] += 1
    else:
        data[a] = 1

for i in range(len(A)):
    while stack and data[stack[-1][0]] < data[A[i]]:
        _, idx = stack.pop()
        ans[idx] = A[i]
    stack.append([A[i], i])

print(*ans)