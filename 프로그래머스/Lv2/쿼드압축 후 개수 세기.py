# https://school.programmers.co.kr/learn/courses/30/lessons/68936

answer = []

def compress(arr):
    global answer

    n = len(arr)
    if n == 1:
        answer[arr[0][0]] += 1
        return 
    
    standard = [0] * 4
    new_arr = [[] for _ in range(4)]

    for i in range(0, n//2):
        new_arr[0].append([])
        new_arr[1].append([])
        new_arr[2].append([])
        new_arr[3].append([])

        for j in range(0, n//2):
            standard[0] += arr[i][j]
            new_arr[0][i].append(arr[i][j])

            standard[1] += arr[i+n//2][j]
            new_arr[1][i].append(arr[i+n//2][j])

            standard[2] += arr[i][j+n//2]
            new_arr[2][i].append(arr[i][j+n//2])

            standard[3] += arr[i+n//2][j+n//2]
            new_arr[3][i].append(arr[i+n//2][j+n//2])


    for i in range(4):
        if standard[i] == (n//2)**2:
            answer[1] += 1
        elif standard[i] == 0:
            answer[0] += 1
        else:
            compress(new_arr[i])
    return

def solution(arr):
    global answer
    answer = [0, 0]
    standard = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            standard += arr[i][j]
    
    if standard == n**2:
        return [0, 1]
    elif standard == 0:
        return [1, 0]
    else:
        compress(arr)
    return answer


print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])) # [1, 0]
print(solution([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])) # [0, 1]

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # [4,9]
print(solution([[1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1],
                [0,0,0,0,1,1,1,1],
                [0,1,0,0,1,1,1,1],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,1],
                [0,0,0,0,1,1,1,1]])) # 	[10,15]



