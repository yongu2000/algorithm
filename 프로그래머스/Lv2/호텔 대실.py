# https://school.programmers.co.kr/learn/courses/30/lessons/155651
import heapq

def parse_time(time):
    return int(time[:2]), int(time[3:5])

def convert_time_to_min(time):
    hour, minute = parse_time(time)
    return hour*60 + minute

def convert_min_to_time(minute):
    h, m = minute // 60, minute % 60
    return f"{h if h >= 10 else str(0)+str(h)}:{m if m >= 10 else str(0)+str(m)}"

def solution(book_time):
    answer = 0  
    book_time.sort()
    min_time = []
    for time in book_time:
        start, end = list(map(convert_time_to_min, time))
        while min_time and min_time[0] <= start:
            heapq.heappop(min_time)
        heapq.heappush(min_time, end+10)
        answer = max(answer, len(min_time))

    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])) # 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]])) # 1
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])) # 3












