class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ans = [0]*(max(nums)+1)

        for i in nums:

            ans[i]+=1
        
        pre_sum = [0]*len(ans)

        for i in range(1,len(pre_sum)):

            pre_sum[i]+= ans[i-1] + pre_sum[i-1]
        for i in range(len(nums)):

            nums[i] = pre_sum[nums[i]]
        return nums