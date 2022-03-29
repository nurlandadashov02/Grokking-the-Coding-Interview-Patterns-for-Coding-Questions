class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def has_path(root, target):
    if root is None:
        return False

    if root.val == target and root.left is None and root.right is None:
        return True

    return has_path(root.left, target - root.val) or has_path(root.right, target - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(str(has_path(root, 16)))


main()