# https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    temp = s[2:-2].split("},{")
    temp = [set(map(int, s.split(","))) for s in temp]
    temp.sort(key=lambda x : len(x))
    answer.append(list(temp[0])[0])
    for i in range(1, len(temp)):
        answer.append(list((temp[i] - temp[i-1]))[0])
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # 2 1 3 4
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # 2 1 3 4
print(solution("{{20,111},{111}}")) # 111 20
print(solution("{{123}}")) # 123
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # 3 2 4 1
print(solution("{{4},{41,4},{4,441,41}}")) #  [4, 41, 441]
print(solution("{{1,2},{1},{1,2,3}}")) #  [1 2 3]




