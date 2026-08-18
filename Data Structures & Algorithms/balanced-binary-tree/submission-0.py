# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        head = root
        balance = True
        def trav(head):
            nonlocal balance
            if not head:
                return 0
            left = trav(head.left)
            right = trav(head.right)
            if abs(right -left)>1:
                balance = False
            
            return max(left,right)+1
        trav(head)
        return balance