# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    nicknames = dict()

    for rec in record:
        r = rec.split()
        if r[0] != "Leave":
            nicknames[r[1]] = r[2]
    for rec in record:
        r = rec.split()
        if r[0] == "Enter":
            answer.append(f"{nicknames[r[1]]}님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(f"{nicknames[r[1]]}님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])) # 5



