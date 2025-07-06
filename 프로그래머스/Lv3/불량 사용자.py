# https://school.programmers.co.kr/learn/courses/30/lessons/64064

import re

n = 0
answer = set()
temp_list = []

def dfs(s, idx):
    global temp_list, answer

    if n == idx:
        answer.add(frozenset(s))
        return

    for temp in temp_list[idx]:
        s.add(temp)
        if len(s) - 1 == idx:
            dfs(s, idx + 1)
            s.discard(temp)    
    return

def solution(user_id, banned_id):
    global n, temp_list, answer

    n = len(banned_id)
    answer = set()
    temp_list = []

    for ban in banned_id:
        temp = []
        reg = ban.replace("*", "[a-z0-9]")
        for idx, user in enumerate(user_id):
            if re.fullmatch(reg, user):
                temp.append(idx)
        
        temp_list.append(temp)
    
    dfs(set(), 0)
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))



