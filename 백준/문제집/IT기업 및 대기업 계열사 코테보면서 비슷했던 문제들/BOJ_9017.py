import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    table = list(map(int, input().split()))

    team_six = []
    for i in set(table):
        if table.count(i) == 6:
            team_six.append(i)
    
    result = [[] for _ in range(201)]
    score = 1
    for i in table:
        if i in team_six:
            result[i].append(score)
            score += 1
    winning_score = sys.maxsize
    for i in team_six:
        top_four = result[i][:4]
        point = sum(top_four)
        winning_score = min(winning_score, point)
        result[i].append(point)

    winning_candidates = []
    for i in team_six:
        if result[i][6] == winning_score:
            winning_candidates.append(i)

    winner = sys.maxsize
    fifth_runner_min = sys.maxsize
    for i in winning_candidates:
        fifth_runner = result[i][4]
        if fifth_runner < fifth_runner_min:
            fifth_runner_min = fifth_runner
            winner = i

    print(winner)