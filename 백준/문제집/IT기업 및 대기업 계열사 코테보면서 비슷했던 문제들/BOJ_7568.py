import sys
input = sys.stdin.readline

n = int(input())
people = []
for i in range(n):
    kg, cm = map(int, input().split())
    people.append([kg, cm])

ans = []
for i in range(n):
    rank = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ans.append(rank)

print(" ".join(map(str, ans)))