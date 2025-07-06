# https://school.programmers.co.kr/learn/courses/30/lessons/81303

from heapq import heappush, heappop

def solution(n, k, cmd):
    answer = list('O'*n)
    top = []
    bottom = []
    undo = []

    for i in range(n):
        if i < k:
            heappush(top, -i)
        else:
            heappush(bottom, i)

    for c in cmd:
        if c[0] == "U":
            _, move = c.split()
            move = int(move)
            for _ in range(move):
                if top:
                    heappush(bottom, -heappop(top))
                if not top:
                    break

        elif c[0] == "D":
            _, move = c.split()
            move = int(move)
            for _ in range(move):
                if bottom:
                    heappush(top, -heappop(bottom))
                if not bottom:
                    heappush(bottom, -heappop(top))
                    break

        elif c[0] ==  "C":
            undo.append(heappop(bottom))
            if not bottom:
                heappush(bottom, -heappop(top))
        else:
            item = undo.pop()
            if item < bottom[0]:
                heappush(top, -item)
            else:
                heappush(bottom, item)
    for i in undo:
        answer[i] = "X"

    return ''.join(answer)

print(solution(8, 2,
                ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
               )) # "OOOOXOOO"
print(solution(8, 2,
                ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
               )) # "OOXOXOOO"


