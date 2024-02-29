# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.num = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def check(root):

            if root:
                self.num = self.num*10+root.val
            if root.left:
                check(root.left)
            if root.right:
                check(root.right)
            if not root.left and not root.right:self.ans.append(self.num)
            self.num = (self.num-root.val)//10 if root else 0
        check(root)

        return sum(self.ans)

        