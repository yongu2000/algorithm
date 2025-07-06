# https://school.programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*4, reverse = True)
    return str(int(''.join(numbers)))


print("1"*4)
print(solution([1, 11, 111, 1111]))
print(solution([565, 56]))
print(solution([232, 23]))
print(solution([212, 21] ))
print(solution([70, 0, 0, 0, 0] ))
print(solution([0, 0, 0, 0]))
print(solution([1000, 111, 110, 101, 100, 11, 10, 1, 0]))
print(solution([1, 10, 100, 1000]))
print(solution([3, 30, 34, 5, 9]))



