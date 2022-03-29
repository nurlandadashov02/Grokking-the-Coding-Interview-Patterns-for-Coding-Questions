class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def count_paths(root, target, path):
    if root is None:
        return 0

    path.append(root.val)
    count, sum = 0, 0
    for i in range(len(path) - 1, -1, -1):
        sum += path[i]
        if sum == target:
            count += 1

    count += count_paths(root.left, target, path) + count_paths(root.right, target, path)

    del path[-1]
    return count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(6)
    print(str(count_paths(root, 19, [])))


main()
