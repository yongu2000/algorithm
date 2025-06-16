# https://school.programmers.co.kr/learn/courses/30/lessons/42860

dictionary = {
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 12,
    "P": 11,
    "Q": 10,
    "R": 9,
    "S": 8,
    "T": 7,
    "U": 6,
    "V": 5,
    "W": 4,
    "X": 3,
    "Y": 2,
    "Z": 1
}

def solution(name):
    answer = 0
    n = len(name)

    for a in name:
        if a != "A":
            answer += dictionary[a]

    move = n - 1
    for i in range(n):
        idx = i+1
        while (idx < n) and (name[idx] == 'A'):
            idx += 1

        distance = min(i,  n - idx)
        move = min(move, i + n - idx + distance)
    answer += move

    return answer


print(solution("BBBAAAAAB")) # 8
print(solution("BBAAAABBB")) # 10












