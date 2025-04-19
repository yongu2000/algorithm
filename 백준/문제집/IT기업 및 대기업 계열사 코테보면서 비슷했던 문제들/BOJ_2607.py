import sys
input = sys.stdin.readline

n = int(input())
word = list(input().strip())
answer = 0
for _ in range(n-1):
    temp = list(input().strip())
    different = 0
    for w in word:
        if w in temp:
            temp.remove(w)
        else:
            different += 1
    if different < 2 and len(temp) < 2:
        answer += 1
print(answer)