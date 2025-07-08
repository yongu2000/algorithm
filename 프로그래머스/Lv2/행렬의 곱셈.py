# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = [[]]

    n1, m1 = len(arr1), len(arr1[0])
    n2, m2 = len(arr2), len(arr2[0])

    answer = [[0] * m2 for _ in range(n1)]

    for i in range(n1):
        for j in range(m2):
            val = 0
            for w in range(m1):
                val += arr1[i][w]*arr2[w][j]
            answer[i][j] = val
    
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])) # [[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]	)) # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]





