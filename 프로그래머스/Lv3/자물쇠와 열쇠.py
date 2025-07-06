# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def solution(key, lock):
    n = len(lock)
    m = len(key)

    def rotate(key):
        new_key = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if key[i][j] == 1:
                    new_key[j][m-1-i] = 1
        return new_key

    def open(key, lock):
        for i in range(m-1, m+n-1):
            for j in range(m-1, m+n-1):
                if key[i][j] == lock[i][j]:
                    return False
        return True

    def shift_key(key, x, y):
        new_key = [[0]*(n+m*2-2) for _ in range(n+m*2-2)]

        for i in range(m):
            for j in range(m):
                new_key[i+x][j+y] = key[i][j]
        return new_key
    keys = [
        key,
        rotate(key),
        rotate(rotate(key)),
        rotate(rotate(rotate(key))),
    ]

    n_lock = [[0]*(n+m*2-2) for _ in range(n+m*2-2)]

    for i in range(m-1, m+n-1):
        for j in range(m-1, m+n-1):
            n_lock[i][j] = lock[i-m+1][j-m+1]

    for key in keys:
        for i in range(n+m-1):
            for j in range(n+m-1):
                if open(shift_key(key, i, j), n_lock):
                    return True                
    return False

print(solution([[0, 0, 0], 
                [1, 0, 0], 
                [0, 1, 1]],
                [[1, 1, 1], 
                 [1, 1, 0], 
                 [1, 0, 1]]
               )) 

