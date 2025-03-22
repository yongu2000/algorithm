import sys
input = sys.stdin.readline

def check_color(n, paper):
    check_blue = True
    check_white = True
    for i in range(n):
        for j in range(n):
            if paper[i][j] == 0:
                check_blue = False
            if paper[i][j] == 1:
                check_white = False
    if check_blue:
        return 1, 0
    if check_white:
        return 0, 1
    return 0, 0


def slice_paper(n, paper):
    blue, white = check_color(n, paper)

    if n == 1:
        return blue, white

    if [blue, white] != [0, 0]:
        return blue, white

    papers = [
        [row[0:n//2] for row in paper[0:n//2]],
        [row[n//2:n] for row in paper[0:n//2]],
        [row[0:n//2] for row in paper[n//2:n]],
        [row[n//2:n] for row in paper[n//2:n]]
    ]
    
    for p in papers:
        b, w = slice_paper(n//2, p)
        blue += b
        white += w

    return blue, white



n = int(input())
paper = list(list(map(int, input().split())) for _ in range(n))

ans = slice_paper(n, paper)
print(ans[1])
print(ans[0])
