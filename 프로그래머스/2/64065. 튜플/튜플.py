def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    
    data = []
    for char in s:
        data.append(set(map(int, char.split(","))))
    data.sort()
    
    temp = set()
    for d in data:
        answer.append((d-temp).pop())
        temp = d
    return answer