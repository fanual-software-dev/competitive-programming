# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums, root = 0):
            if len(nums)==1:
                root = nums[0]
                return TreeNode(root)
            elif len(nums)==0:
                return None
            else:
                i = len(nums)//2
                root = nums[i]
                left = build(nums[:i])
                right = build(nums[i+1:])
                return TreeNode(root,left,right)
        return build(nums)
        
        