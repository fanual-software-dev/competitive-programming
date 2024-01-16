class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        presum = [0]*(len(nums)+1)
        ans = 0
        for i in range(len(nums)):
            presum[i+1] = presum[i]+nums[i]
        
        for i in range(1,len(nums)):
            if presum[i]>=presum[-1]-presum[i]:
                ans+=1
        return ans
        