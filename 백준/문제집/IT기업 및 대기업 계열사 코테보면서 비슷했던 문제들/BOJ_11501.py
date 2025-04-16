import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    stock_price = sorted(list(set(stocks)))

    profit = 0
    stock_count = 0

    target_price = stock_price[-1]
    stocks_dict = dict()
    
    for s in stocks:
        if s in stocks_dict:
            stocks_dict[s] += 1
        else:
            stocks_dict[s] = 1

    for s in stocks:
        while stocks_dict[target_price] == 0:
            stock_price.pop()
            target_price = stock_price[-1]
        if s != target_price:
            profit -= s
            stock_count += 1
        if s == target_price and stock_count > 0:
            profit += stock_count*s
            stock_count = 0
        stocks_dict[s] -= 1
    print(profit)
