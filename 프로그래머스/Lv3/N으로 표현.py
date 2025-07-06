# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    dp = [set() for _  in range(9)]


    for i in range(1, 9):

        dp[i].add(int(str(N)*i))

        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:

                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y!= 0:
                        dp[i].add(x//y)

                    if number in dp[i]:
                        return i
        
        if number in dp[i]:
            return i
            
    return -1

print(solution(5, 12)) # 4
print(solution(2, 11)) # 3












