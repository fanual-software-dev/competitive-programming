# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def l_common(root,ans = None):
            if not root:
                return ans
            if root.val==p.val or root.val==q.val:
                return root
            elif (root.val>p.val and root.val<q.val) or (root.val<p.val and root.val>q.val):
                return root
            elif (root.val>p.val and root.val>q.val):
                return l_common(root.left)
            elif  (root.val<p.val and root.val<q.val):
                return l_common(root.right)
    
        return l_common(root)

        