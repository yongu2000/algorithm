import sys
input = sys.stdin.readline

n = int(input())

stack = []
answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        stack.pop()
        answer += 1
    if not stack or stack and stack[-1] != y:
        if y != 0:
            stack.append(y)

answer += len(stack)
print(answer)