from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    data = defaultdict(int)
    
    for t in tangerine:
        data[t] += 1
    sorted_data = sorted(data.items(), key=lambda x : x[1], reverse=True)
    
    for _, val in sorted_data:
        if k > val:
            k -= val
            answer += 1
        else:
            answer += 1
            break

    return answer