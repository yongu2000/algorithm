import sys
input = sys.stdin.readline

data = list(input().strip())
bomb = list(input().strip())
bomb_len = len(bomb)
stack = []

for d in data:
    stack.append(d)
    if len(stack) < bomb_len:
        continue
    
    temp = stack[-bomb_len:]

    if temp == bomb:
        stack = stack[:-bomb_len]
if stack:
    print("".join(stack))
else:
    print("FRULA")
