# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def check(root,l,h):
            if l<=root.val<=h:
                self.ans+=root.val
                
            if root.left:check(root.left,l,h)
            if root.right:check(root.right,l,h)
        check(root,low,high)
        return self.ans
        