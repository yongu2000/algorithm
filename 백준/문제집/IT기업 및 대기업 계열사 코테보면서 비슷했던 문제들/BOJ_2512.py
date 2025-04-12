import sys
input = sys.stdin.readline


def calc_budget(mid):
    total = gov_budget
    for b in budgets:
        if mid > b:
            total -= b
        else:
            total -= mid
    if total >= 0:
        return True
    return False

n = int(input())
budgets = list(map(int, input().split()))
gov_budget = int(input())

left = 0
right = max(budgets)

while left <= right:
    mid = (left + right) // 2

    if calc_budget(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)