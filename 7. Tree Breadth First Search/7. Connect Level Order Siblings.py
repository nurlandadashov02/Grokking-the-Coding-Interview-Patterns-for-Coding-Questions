from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None


def traverse(root):
    lastNode = None
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        levelSize = len(queue)
        for _ in range(levelSize):
            node = queue.popleft()
            if lastNode:
                lastNode.next = node
            lastNode = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        lastNode = None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    traverse(root)



main()
