class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def sum_path_numbers(root):
    def dfs(_root, num):
        if _root is None:
            return 0

        if _root.left is None and _root.right is None:
            return int(num)

        left, right = 0, 0
        if _root.left:
            left = dfs(_root.left, num + str(_root.left.val))
        if _root.right:
            right = dfs(_root.right, num + str(_root.right.val))
        return left + right

    return dfs(root, str(root.val))


def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print(str(sum_path_numbers(root)))


main()
