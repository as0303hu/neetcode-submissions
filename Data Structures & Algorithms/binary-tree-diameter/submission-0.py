# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def trav(head):
            nonlocal maxi

            if not head:
                return 0

            left = trav(head.left)
            right = trav(head.right)

            count = left + right
            maxi = max(maxi, count)

            return max(left, right) + 1

        trav(root)
        return maxi