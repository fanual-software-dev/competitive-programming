class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        pre_sum = [0]*(len(nums)+2)

        for i in range(len(nums)):
            pre_sum[i+1] = pre_sum[i]+nums[i]
            
        for i in range(len(nums)):
            nums[i] = (nums[i]*(i) - pre_sum[i])+(pre_sum[len(nums)]-pre_sum[i+1]-nums[i]*(len(nums)-i-1))
        return nums
        