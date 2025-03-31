import sys

equi = "Equilateral"
iso = "Isosceles"
scal = "Scalene"
invalid = "Invalid"

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    num_list = [a, b, c]
    num_set = set(num_list)
    max_num = max(num_list)

    num_list.remove(max_num)
    if max_num >= sum(num_list):
        print(invalid)
        continue
    if a == 0 or b == 0 or c == 0:
        print(invalid)
        continue

    if len(num_set) == 3:
        print(scal)
        continue

    if len(num_set) == 2:
        print(iso)
        continue

    if len(num_set) == 1:
        print(equi)
        continue