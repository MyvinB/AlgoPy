from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepthQueue(root: TreeNode) -> int:
    queue = deque()
    queue.append(root)
    depth = 1
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if node.right is None and node.left is None:
                return depth
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        depth = depth + 1


def minDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        1 + self.minDepth(root.right)
    if root.right is None:
        1 + self.minDepth(root.left)
    left = self.minDepth(root.left)
    right = self.minDepth(root.right)
    return min(left, right) + 1


def main():
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.right.right = TreeNode(5)
    print(minDepthQueue(node))


if __name__ == "__main__":
    main()
