import sys
input = sys.stdin.readline

n, score, p = map(int, input().split())
ranking = list(map(int, input().split()))

if n == 0:
    print(1)
else:
    if score > ranking[0]:
        print(1)
        exit()
    index = -1
    for i in range(n):
        if score >= ranking[i]:
            index = i
            break
    count = 0
    for i in range(n):
        if score <= ranking[i]:
            count += 1
    if count >= p:
        print(-1)
    else:
        if index == -1:
            print(count+1)
        else:
            print(index+1)