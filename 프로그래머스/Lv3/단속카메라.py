# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    camera = -30001
    routes.sort(key = lambda x: x[1])
    for route in routes:
        start, end = route

        if camera < start:
            camera = end
            answer += 1
        
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))


