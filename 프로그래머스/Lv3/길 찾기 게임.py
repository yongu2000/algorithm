# https://school.programmers.co.kr/learn/courses/30/lessons/42892

def solution(nodeinfo):
    info = [sublist + [idx+1] for idx, sublist in enumerate(nodeinfo)]
    pre = []
    post = []
    class Node:
        def __init__(self, x, y, val):
            self.x = x
            self.y = y
            self.val = val
            self.left = None
            self.right = None

    def insert(parent, child):
        if child.x < parent.x:
            if parent.left is None:
                parent.left = child
            else:
                insert(parent.left, child)
        else:
            if parent.right is None:
                parent.right = child
            else:
                insert(parent.right, child)

    def preorder(node): 
        if node:
            pre.append(node.val)
            preorder(node.left)
            preorder(node.right)

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            post.append(node.val)

    info.sort(key=lambda x: (-x[1], x[0]))
    root = Node(info[0][0], info[0][1], info[0][2])
    for x, y, idx in info[1:]:
        insert(root, Node(x, y, idx))

    preorder(root)
    postorder(root)
    return [pre, post]

print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])) 
# [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]


