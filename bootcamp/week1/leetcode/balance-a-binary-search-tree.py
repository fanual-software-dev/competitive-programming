# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder(root,ans = []):
            if root :
                ans.append(root.val)
            if root.left:
                inorder(root.left)
            if root.right:
                inorder(root.right)
            return ans
        ans = inorder(root)
        ans.sort()

        def divide(root):

            if len(root)==0:
                return None
            if len(root)==1:
                return TreeNode(root[0])
            else:
                mid = len(root)//2
                num = TreeNode(root[mid])
                num.left = divide(root[:mid])
                num.right = divide(root[mid+1:])
            return num
        return divide(ans)
        