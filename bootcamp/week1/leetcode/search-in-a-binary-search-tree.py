# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return root
        def check(root,val):

            if root.val==val:
                self.ans.append(root)
        
            if root.left and val<root.val:
                check(root.left,val)
            elif root.right and val>root.val:
                check(root.right,val)
        
            
            
        check(root,val)
        return self.ans[0] if self.ans else None