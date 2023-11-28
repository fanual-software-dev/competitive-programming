class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        ans=0
        left,right=0,len(nums)-1

        while left<=right:
            if nums[left]<=nums[right]:
                ans=max(ans,nums[left]*(right-left))
                left+=1
            else:
                ans=max(ans,nums[right]*(right-left))
                right-=1
        return ans