# https://school.programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict

def solution(gems):
    answer = []
    
    gem_cnt = len(set(gems))
    count = defaultdict(int)
    temp = set()
    
    left = 0
    right = 0
    
    count[gems[0]] += 1
    temp.add(gems[0])
    
    if len(temp) == gem_cnt:
        answer = [1, 1]
    
    while left <= right and right <= len(gems)-1:
        if len(temp) == gem_cnt:
            count[gems[left]] -= 1
            if count[gems[left]] == 0:
                temp.discard(gems[left])
            left += 1
        else:
            right += 1
            count[gems[right]] += 1
            temp.add(gems[right])
    
        if len(temp) == gem_cnt:
            if not answer:
                answer = [left+1, right+1]
            else:
                ans_l, ans_r = answer
                if right - left < ans_r - ans_l:
                    answer = [left+1, right+1]
        elif len(temp) != gem_cnt and right == len(gems) - 1:
            break
    
    return answer

# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["A" , "B","B","B","C", "D","D" ,"D" ,"D" ,"D" ,"D","D" ,"B" ,"C" ,"A"]))