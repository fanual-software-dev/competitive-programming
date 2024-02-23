# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def search(root,k):
            if root.left:
                search(root.left,k)
            self.ans.append(root.val)
            if root.right:search(root.right,k)
        search(root,k)
        return self.ans[k-1]