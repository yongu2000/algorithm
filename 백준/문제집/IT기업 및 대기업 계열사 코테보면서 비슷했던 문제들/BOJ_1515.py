import sys
from collections import deque
input = sys.stdin.readline

number = list(input().strip())

i = 1
while True:
    temp = deque(str(i))
    while temp:
        t = temp.popleft()
        if number and number[0] == t:
            del number[0]
    if not number:
        break
    i += 1
print(i)