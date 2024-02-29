# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def check(nums):
            if len(nums)==0:
                return None
            if len(nums)==1:
                return TreeNode(nums[0])
            m = nums.index(max(nums))

            root = TreeNode(nums[m])

            root.left = check(nums[:m])
            root.right = check(nums[m+1:])

            return root
        return check(nums)            
        