# https://school.programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    answer = []

    dictionary = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26

    }

    idx = 0
    dict_idx = 26
    while idx < len(msg):
        m = msg[idx]
        while m in dictionary:
            idx += 1
            if idx >= len(msg):
                break
            m += msg[idx]

        dict_idx += 1
        if m not in dictionary:
            dictionary[m] = dict_idx

        if idx >= len(msg):
            answer.append(dictionary[m])
        else:
            answer.append(dictionary[m[:-1]])

    return answer


print(solution("KAKAO")) # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT"))  # 	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34] 
print(solution("ABABABABABABABAB")) # 	[1, 2, 27, 29, 28, 31, 30]