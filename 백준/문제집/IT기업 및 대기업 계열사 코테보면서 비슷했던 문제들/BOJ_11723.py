import sys
input = sys.stdin.readline

m = int(input())
S = set()

for _ in range(m):
    command = input().strip().split()

    if len(command) == 2:
        operation, num = command[0], command[1]
        num = int(num)
        if operation == "add":
            S.add(num)
        elif operation == "remove":
            S.discard(num)
        elif operation == "check":
            print(1) if num in S else print(0)
        elif operation == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
    else:
        if command[0] == "all":
            S = set([i for i in range(1, 21)])
        elif command[0] == "empty":
            S = set()