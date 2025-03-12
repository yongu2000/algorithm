import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

stack = []
ans = [-1] * n
for i in range(len(A)):

    while stack and stack[-1][0] < A[i]:
        _, idx = stack.pop()
        ans[idx] = A[i]
    stack.append([A[i], i])

print(*ans)