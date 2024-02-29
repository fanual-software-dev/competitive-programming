# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        seen = defaultdict(int)
        def check(root,seen):

            if root:
                seen[root.val]+=1
            if root.left:check(root.left,seen)
            if root.right:check(root.right,seen)
        check(root,seen)

        ans = []
        if len(seen)>1:
            m = max(seen.values()) 
        else:
            for i in seen.values():
                m = i

        for key,value in seen.items():

            if value==m:
                ans.append(key)
        return ans



            

        