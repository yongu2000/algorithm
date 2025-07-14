# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0

    skill_set = set(skill)
    for skill_tree in skill_trees:
        sequence = 0
        flag = True
        for s in skill_tree:
            if s not in skill_set:
                continue
            else:
                if s == skill[sequence]:
                    sequence += 1
                else:
                    flag = False
                    break
        
        if flag:
            answer += 1
            
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))



