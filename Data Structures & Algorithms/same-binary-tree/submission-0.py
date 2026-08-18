# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        def travers(p,q):
            nonlocal same
             # Both nodes are None
            if not p and not q:
                return

            # One node is None, other is not
            if not p or not q:
                same = False
                return
            if p.val != q.val:
                same =False
                return
            left = travers(p.left,q.left)
            right = travers(p.right,q.right)
            return
        travers(p,q)
        return same

        