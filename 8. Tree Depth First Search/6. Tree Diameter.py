class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    def diameter(self, root):
        self.height(root)
        return self.treeDiameter

    def height(self, root):
        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        diameter = left + right + 1
        self.treeDiameter = max(self.treeDiameter, diameter)

        return max(left, right) + 1


def main():
    treeDiameter = TreeDiameter()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print(str(treeDiameter.diameter(root)))

    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print(str(treeDiameter.diameter(root)))


main()
