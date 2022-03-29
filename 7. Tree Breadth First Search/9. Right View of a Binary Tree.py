from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        result.append(list(queue)[-1].val)
        for _ in range(levelSize):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.left.left = TreeNode(3)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(str(traverse(root)))


main()
