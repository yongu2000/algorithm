import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belts = deque(map(int, input().split()))

durability = 0
ans = 0
start, end = 0, n-1

robots = deque()
while True:
    ans += 1

    belts.appendleft(belts.pop())
    ended = False
    for i in range(len(robots)):
        robots[i] = robots[i]+1
        if robots[i] == end:
            ended = True

    if ended:
        robots.popleft()

    ended = False
    for i, r in enumerate(robots):
        curr_position = r 

        if curr_position + 1 <= end and belts[curr_position + 1] > 0 and curr_position + 1 not in robots:
            

            curr_position += 1
            robots[i] = curr_position
            belts[curr_position] -= 1

            if curr_position == end:
                ended = True

            if belts[curr_position] == 0:
                durability += 1
        
    if ended:
        robots.popleft()
    
    if belts[start] > 0:
        robots.append(start)
        belts[start] -= 1
        if belts[start] == 0:
            durability += 1
    
    if durability >= k:
        break
    
print(ans)
