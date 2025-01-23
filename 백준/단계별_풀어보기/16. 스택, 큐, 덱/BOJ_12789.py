n = int(input())
students = map(int, input().split())
order = 1
stack = []

for s in students:
    if s == order:
        order += 1
    elif s != order:
        stack.append(s)
    while (len(stack) > 0 and stack[len(stack) - 1] == order):
        order += 1
        stack.pop()

if len(stack) == 0:
    print("Nice")
else:
    print("Sad")