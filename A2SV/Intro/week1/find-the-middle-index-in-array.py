class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        presum = [0]*len(nums)
        presum[0] = nums[0]
        for i in range(1,len(nums)):
            presum[i] = presum[i-1]+nums[i]
        for i in range(len(presum)):
            if presum[i]-nums[i]==presum[-1]-presum[i]:
                return i
        return -1
        