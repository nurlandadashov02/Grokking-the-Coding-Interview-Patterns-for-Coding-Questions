class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class TreeDiameter:
    def __init__(self):
        self.maxSum = 0

    def diameter(self, root):
        self.height(root)
        return self.maxSum

    def height(self, root):
        if root is None:
            return 0

        left = max(self.height(root.left), 0)
        right = max(self.height(root.right), 0)

        diameter = left + right + root.val
        self.maxSum = max(self.maxSum, diameter)

        return max(left, right) + root.val


def main():
    treeDiameter = TreeDiameter()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)

    root.right.right.left = TreeNode(9)
    print(str(treeDiameter.diameter(root)))


main()
