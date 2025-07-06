# https://school.programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    member_idx = dict()
    member_graph = [-1] * len(enroll)
    for idx, member in enumerate(enroll):
        member_idx[member] = idx

    for i in range(len(enroll)):
        parent = referral[i]
        if parent == "-":
            continue
        member_graph[i] = member_idx[parent]

    for i in range(len(seller)):
        s = member_idx[seller[i]]

        price = amount[i] * 100

        while s != -1:
            answer[s] += price - price // 10
            s = member_graph[s]
            price = price // 10
            if price < 1:
                break
        
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]
               )) # [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]
               )) # [0, 110, 378, 180, 270, 450, 0, 0]
