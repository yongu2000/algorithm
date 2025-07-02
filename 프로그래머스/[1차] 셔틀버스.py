# https://school.programmers.co.kr/learn/courses/30/lessons/17678

def parse_time(time):
    return int(time[:2]), int(time[3:5])

def convert_time_to_min(time):
    hour, minute = parse_time(time)
    return hour*60 + minute

def convert_min_to_time(minute):
    h, m = minute // 60, minute % 60
    return f"{h if h >= 10 else str(0)+str(h)}:{m if m >= 10 else str(0)+str(m)}"

def solution(n, t, m, timetable):
    answer = ''

    timetable = list(map(convert_time_to_min, timetable))
    timetable.sort(reverse=True)

    bus_time = 9*60 - t
    for _ in range(n-1): ### 앞차 보내고 인원 줄이기
        bus_time += t ### 승차 시각
        for _ in range(m): ### 최대, 좌석수(m) 만큼
            if timetable and timetable[-1]<=bus_time:
                timetable.pop()
            else: ### skip 
                break

    bus_time += t ### 콘이 승차할 막차 시각
    answer = bus_time if len(timetable)< m or timetable[-m]>bus_time else timetable[-m] -1
    # timetable 정원이 남았거나, timeTable에 남은 사람 중 첫 사람이 막차시간보다 느리면 막차시간에 딱 타기
    # 아니라면 마지막 사람 1분 전에 타기
    return convert_min_to_time(answer)

print(solution(3, 1, 2,
                ["06:00", "23:59", "05:48", "00:01", "00:01"]
               )) # 	  "09:02"