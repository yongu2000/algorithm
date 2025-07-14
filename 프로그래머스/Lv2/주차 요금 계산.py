# https://school.programmers.co.kr/learn/courses/30/lessons/92341
from collections import defaultdict
import math

def time_to_min(time):
    hour, min = time.split(":")

    return int(hour)*60 + int(min)

def solution(fees, records):
    answer = []

    data = defaultdict(int)
    base, base_fee, add, add_fee = fees

    for record in records:
        time, car_num, action = record.split()
        time = time_to_min(time)
        if action == "IN":
            data[car_num] -= time
        else:
            data[car_num] += time

    for _, val in sorted(data.items()):
        if val <= 0:
            val += time_to_min("23:59")

        if val <= base:
            answer.append(base_fee)
        elif val > base:
            val -= base
            answer.append(base_fee + math.ceil(val / add)*add_fee)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], 	["00:00 1234 IN"]))



