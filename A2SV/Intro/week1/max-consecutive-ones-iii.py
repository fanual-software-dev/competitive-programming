class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = k
        ans = left = 0

        for right in range(len(nums)):

            if nums[right]==0:
                count-=1
            while count<0:
                if nums[left]==0:
                    count+=1
                left+=1
            ans = max(ans,right-left+1)
        return ans