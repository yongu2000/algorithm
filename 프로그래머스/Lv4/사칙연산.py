# https://school.programmers.co.kr/learn/courses/30/lessons/1843
import sys

n = 0
MAX_DP = []
MIN_DP = []

def solution(arr):
    global n, MAX_DP, MIN_DP
    INF = sys.maxsize
    n = len(arr) // 2 + 1
    operands = []
    numbers = []

    for i in range(len(arr)):
        if i % 2 == 0:
            numbers.append(int(arr[i]))
        else:
            operands.append(arr[i])
    print(operands, numbers)

    MAX_DP = [[-INF]*(n+1) for _ in range(n+1)]
    MIN_DP = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        MAX_DP[i][0] = 0
        MAX_DP[0][i] = 0

        MIN_DP[i][0] = 0
        MIN_DP[0][i] = 0

    for i in range(1, n+1):
        MAX_DP[1][i] = numbers[i-1]
        MIN_DP[1][i] = numbers[i-1]

    for i in range(2, n+1):
        for j in range(1, i):
            print(i, j)
            print(numbers[i], operands[j-1])
                
            



    print(MAX_DP, MIN_DP)

    print(n)
    answer = -1
    return answer

print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
