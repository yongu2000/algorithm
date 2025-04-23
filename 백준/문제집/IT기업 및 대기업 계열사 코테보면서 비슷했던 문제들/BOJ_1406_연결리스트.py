import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

string = input().strip()

head = Node("head")
cursor = head

for s in string:
    temp = Node(s)
    cursor.next = temp
    temp.prev = cursor
    cursor = temp
    
m = int(input())

for _ in range(m):
    operation = input().strip()

    if operation[0] == "L":
        if cursor.data != "head":
            cursor = cursor.prev
    elif operation[0] == "D":
        if cursor.next != None:
            cursor = cursor.next
    elif operation[0] == "B":
        if cursor.data != 'head':
            cursor = cursor.prev
            if cursor.next.next:
                cursor.next = cursor.next.next
                cursor.next.prev = cursor
            else:
                cursor.next = None
    else:
        _, val = operation.split()
        node = Node(val)
        if cursor.next:
            node.next = cursor.next
            cursor.next.prev = node
        cursor.next = node
        node.prev = cursor
        cursor = node

print_node = head.next
while print_node:
    print(print_node.data, end='')
    print_node = print_node.next