class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def path_with_sequence(root, sequence):
    def dfs(_root, _sequence):
        if _root is None or _sequence[0] != _root.val:
            return False

        if _root.left is None and _root.right is None and \
                len(_sequence) == 1:
            return True

        return dfs(_root.left, _sequence[1:]) or dfs(_root.right, _sequence[1:])

    return dfs(root, sequence)


def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print(str(path_with_sequence(root, [1, 9, 9])))


main()
