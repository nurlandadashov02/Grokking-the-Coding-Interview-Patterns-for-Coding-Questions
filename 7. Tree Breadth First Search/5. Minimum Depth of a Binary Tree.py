from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = 0
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        result += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            node = queue.popleft()
            if not (node.left or node.right):
                return result
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    # root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    # root.right.left.left = TreeNode(11)
    root.right.right = TreeNode(5)
    print(str(traverse(root)))


main()
