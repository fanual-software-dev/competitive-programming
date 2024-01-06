class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = maxt = 0
        
        count = 1
        for right in range(len(nums)):
            if nums[right]==0:
                count-=1
            while count<0:
                if nums[left]==0:
                    count+=1
                left+=1
            
            
            maxt=max(maxt,right-left)
            
        return maxt
            