# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(root):
            if root.left:
                search(root.left)
            self.ans.append(root.val)
            if root.right:search(root.right)
        search(root)
        b = set(self.ans)
        
        return self.ans==sorted(set(self.ans))

        