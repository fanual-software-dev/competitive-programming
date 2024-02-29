# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans1 = []
        count = 0
        queue = []
        zigzag = True
        if root:
            queue.append(root)
        while len(queue)>count:
            ans = []
            for i in range(count,len(queue)):
                ans.append(queue[i].val)
                count+=1
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            if ans:
                if zigzag:
                    ans1.append(ans)
                    zigzag = False
                else:
                    ans1.append(ans[::-1])
                    zigzag = True
        return ans1
                
        