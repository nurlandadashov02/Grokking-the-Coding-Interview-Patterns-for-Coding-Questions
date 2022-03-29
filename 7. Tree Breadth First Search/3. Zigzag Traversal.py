from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    queue = deque()
    queue.append(root)

    right = True

    while queue:
        levelSize = len(queue)
        level = deque()
        for _ in range(levelSize):
            node = queue.popleft()
            if right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level))
        right = not right

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    root.right.right = TreeNode(5)
    print(str(traverse(root)))


main()
