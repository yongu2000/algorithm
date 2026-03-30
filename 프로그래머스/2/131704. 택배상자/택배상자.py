def solution(order):
    answer = 0
    belt = [i for i in range(len(order), 0, -1)]
    temp = []
    
    idx = 0
    while idx < len(order):
        loaded = False
        target = order[idx]
        
        if temp and temp[-1] == target:
            temp.pop()
            answer += 1
            idx += 1
            loaded = True
        
        if not loaded:
            while belt and belt[-1] != target:
                temp.append(belt.pop())
            if belt and belt[-1] == target:
                belt.pop()
                answer += 1
                idx += 1
                loaded = True

        if not loaded:
            break

    return answer