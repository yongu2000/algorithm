# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    visited = set()
    x, y = 0, 0
    for dir in dirs:
        if dir == "U":
            nx, ny = x+0, y+1
        elif dir == "D":
            nx, ny = x+0, y-1
        elif dir == "L":
            nx, ny = x-1, y+0
        else:
            nx, ny = x+1, y+0

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add(((x, y), (nx, ny)))
            visited.add(((nx, ny), (x, y)))
            x, y = nx, ny

    return len(visited) // 2


print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7




