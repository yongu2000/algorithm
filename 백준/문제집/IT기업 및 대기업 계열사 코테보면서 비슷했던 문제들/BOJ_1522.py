import sys
input = sys.stdin.readline

string = input().strip()
length = len(string)
a = string.count("a")

string += string[:a]

max_a = []
max_a_count = -1
for i in range(length):
    temp = string[i:i+a]
    temp_count = temp.count("a")
    if max_a_count < temp_count:
        max_a_count = temp_count
        max_a = temp
print(max_a.count("b"))