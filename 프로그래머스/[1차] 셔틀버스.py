# https://school.programmers.co.kr/learn/courses/30/lessons/17678
from collections import deque

def parse_time(time):
    return int(time[:2]), int(time[3:5])

def convert_time(hour, minute):
    return f"{hour if hour >= 12 else str(0)+str(hour)}:{minute if minute >= 10 else str(0)+str(minute)}"

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()

    people = deque(timetable)
    hour = 9
    minute = 0
    print(people)
    for _ in range(n-1):
        time = convert_time(hour, minute)
        count = 0
        while people[0] <= time:
            count += 1
            people.popleft()
            if count == m :
                break
        hour += (minute + t) // 60
        minute += (minute + t) % 60

    print(people)
        
    return answer


print(solution(2, 10, 2,
               ["09:10", "09:10", "09:09", "08:00", "09:09", "09:25"]
               )) # 	"09:08"
print(solution(1, 1, 5,
               	["08:00", "08:01", "08:02", "08:03"]
               )) # 	"09:00"
print(solution(2, 10, 2,
               ["09:10", "09:10", "09:09", "08:00"]
               )) # 	"09:09"
print(solution(2, 1, 2,
               	["09:00", "09:00", "09:00", "09:00"]
               )) # 	"08:59"
print(solution(1, 1, 5,
               		["00:01", "00:01", "00:01", "00:01", "00:01"]
               )) # 	"00:00"
print(solution(1, 1, 1,
               		["23:59"]
               )) # 	"09:00"
print(solution(10, 60, 45,
               		["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
               )) # 	"18:00"