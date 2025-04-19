import sys
input = sys.stdin.readline

def calculate_area(data):
    area = 0
    height = 0
    prev_index = data[0][0]
    curr_index = 0

    for position in data:
        if position[1] >= height:
            curr_index = position[0]
            area += abs(curr_index - prev_index) * height

            prev_index = position[0]
            height = position[1]
    return area


n = int(input())
columns = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x : x[0])

left_columns = []
right_columns = []

max_column = max(columns, key=lambda x : x[1])
for c in columns:
    if c[0] <= max_column[0]:
        left_columns.append(c)
    if c[0] >= max_column[0]:
        right_columns.append(c)

ans = 0
if left_columns:
    ans += calculate_area(left_columns)
if right_columns:
    right_columns.reverse()
    ans += calculate_area(right_columns)
ans += max_column[1]

print(ans)