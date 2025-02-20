import sys
input = sys.stdin.readline

def check_color(n, data):
    check_black = True
    check_white = True
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                check_black = False
            if data[i][j] == 1:
                check_white = False
    if check_black:
        return 1
    if check_white:
        return 0
    return -1


def slice_data(n, data):
    result = check_color(n, data)
    string = "("
    if n == 1:
        return result

    if result != -1:
        string += str(result)
        return result

    datas = [
        [row[0:n//2] for row in data[0:n//2]],
        [row[n//2:n] for row in data[0:n//2]],
        [row[0:n//2] for row in data[n//2:n]],
        [row[n//2:n] for row in data[n//2:n]]
    ]
    
    for d in datas:
        r = slice_data(n//2, d)
        string += str(r)
    string += ")"
    return string

n = int(input())
data = list(list(map(int, list(input().strip()))) for _ in range(n))
print(slice_data(n, data))