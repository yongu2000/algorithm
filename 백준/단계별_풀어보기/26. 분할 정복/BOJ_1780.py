import sys
input = sys.stdin.readline

def check_num(n, paper):
    check_neg = True
    check_zero = True
    check_one = True
    for i in range(n):
        for j in range(n):
            if paper[i][j] == -1:
                check_zero = False
                check_one = False
            if paper[i][j] == 0:
                check_one = False
                check_neg = False
            if paper[i][j] == 1:
                check_zero = False
                check_neg = False
    if check_neg:
        return 1, 0, 0
    if check_zero:
        return 0, 1, 0
    if check_one:
        return 0, 0, 1
    return 0, 0, 0


def slice_paper(n, paper):
    neg, zero, one = check_num(n, paper)

    if n == 1:
        return neg, zero, one

    if [neg, zero, one] != [0, 0, 0]:
        return neg, zero, one

    papers = [
        [row[0:n//3] for row in paper[0:n//3]],
        [row[n//3:(n//3)*2] for row in paper[0:n//3]],
        [row[(n//3)*2:n] for row in paper[0:n//3]],

        [row[0:n//3] for row in paper[n//3:(n//3)*2]],
        [row[n//3:(n//3)*2] for row in paper[n//3:(n//3)*2]],
        [row[(n//3)*2:n] for row in paper[n//3:(n//3)*2]],

        [row[0:n//3] for row in paper[(n//3)*2:n]],
        [row[n//3:(n//3)*2] for row in paper[(n//3)*2:n]],
        [row[(n//3)*2:n] for row in paper[(n//3)*2:n]],
    ]
    
    for p in papers:
        ne, z, o = slice_paper(n//3, p)
        neg += ne
        zero += z
        one += o
    return neg, zero, one



n = int(input())
paper = list(list(map(int, input().split())) for _ in range(n))

ans = slice_paper(n, paper)
for a in ans:
    print(a)
