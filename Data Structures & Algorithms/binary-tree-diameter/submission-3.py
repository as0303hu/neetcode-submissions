# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = 0
        def trav(head):
            nonlocal maximum

            if not head:
                return 0

            left = trav(head.left)
            right = trav(head.right)

            count = left + right
            maximum = max(maximum, count)

            return max(left, right) + 1

        trav(root)
        return maximum