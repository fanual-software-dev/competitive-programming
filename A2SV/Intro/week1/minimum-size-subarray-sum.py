class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ans=len(nums)+1
        total = left = 0
        for right,n in enumerate(nums):
            total+=n
            while total>=target and left<=right:
                ans= min(ans,right-left+1)
                total-=nums[left]
                left+=1
            
            
        return ans if ans!=len(nums)+1 else 0
            

