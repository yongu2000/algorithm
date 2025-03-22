import sys
input = sys.stdin.readline

def solve(num, count):
    global answer
    if count == n//2:
        teamA = 0
        teamB = 0

        for i in range(n):
            for j in range(n):
                if team[i] and team[j]:
                    teamA += s[i][j]
                if not team[i] and not team[j]:
                    teamB += s[i][j]

        answer = min(answer, abs(teamA-teamB))
        return         

    for i in range(num, n):
        if not team[i]:
            team[i] = True
            solve(i, count+1)
            team[i] = False

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

answer = 90*100 + 1
team = [False] * n
solve(0, 0)
print(answer)