class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = total = 0

        for right in range(len(nums)):

            if nums[right]==1:
                total+=1
            else:
                ans = max(ans,total)
                total=0
        
        return max(ans,total)
                