def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

# 재귀 피보나치의 경우 수많은 1이 더해져 피보나치의 값이 나오기 때문에,
# 피보나치 수의 값과 실행 횟수가 동일함

def fib_dp(n, count_dp):
    dp = [1, 1]
    for i in range(2, n):
        count_dp += 1
        dp.append(dp[i-1]+dp[i-2])
    return dp[n-1], count_dp

n = int(input())

count_rec, count_dp = fib_dp(n, 0)

print(count_rec, count_dp)