answer = 0

op_idx = {"U": 0, "L":1, "R":2, "D":3}
op = [[0, 1], [-1, 0], [1, 0], [0, -1]]

def solution(dirs):
    global answer
    
    visited = list()
    x = 0
    y = 0
    
    for dir in dirs:
        dx, dy = op[op_idx[dir]]
        nx = x + dx
        ny = y + dy
        
        if not (-5 <= nx <= 5) or not (-5 <= ny <= 5):
            continue

        if [x, y, op_idx[dir]] not in visited and [nx, ny, 3 - op_idx[dir]] not in visited:
            answer += 1
            visited.append([x, y, op_idx[dir]])
            visited.append([nx, ny, 3 - op_idx[dir]])
        
        x = nx
        y = ny
    
    return answer