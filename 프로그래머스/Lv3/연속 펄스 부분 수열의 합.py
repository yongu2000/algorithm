# https://school.programmers.co.kr/learn/courses/30/lessons/161988


def solution(sequence):
    answer = 0
    n = len(sequence)
    pulse_p = [num * pow(-1, idx) for idx, num in enumerate(sequence)]
    pulse_n = [num * pow(-1, idx+1) for idx, num in enumerate(sequence)]

    p_sum = [0] * (n+1)
    n_sum = [0] * (n+1)

    for i in range(n):
        p_sum[i+1] = pulse_p[i] + p_sum[i]
        n_sum[i+1] = pulse_n[i] + n_sum[i]

    p_max = max(p_sum)
    p_min = min(p_sum)

    n_max = max(n_sum)
    n_min = min(n_sum)

    answer = max(p_max - p_min, n_max - n_min)

    return answer

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))


