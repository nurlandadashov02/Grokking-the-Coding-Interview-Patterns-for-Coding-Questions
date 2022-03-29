from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def all_paths(root, target):
    paths = dfs(root, target)
    return [list(p) for p in paths]


def dfs(root, target):
    if root is None:
        return None

    if root.val == target and root.left is None and root.right is None:
        return [deque([root.val])]

    left = dfs(root.left, target - root.val)
    right = dfs(root.right, target - root.val)
    ret = []
    if left:
        for el in left:
            el.appendleft(root.val)
        ret += left
    if right:
        for el in right:
            el.appendleft(root.val)
        ret += right

    if len(ret) > 0:
        return ret
    else:
        return None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(str(all_paths(root, 23)))


main()
