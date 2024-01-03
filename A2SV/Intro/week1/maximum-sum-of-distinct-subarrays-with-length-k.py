class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        ans_dict = {}
        left,total = 0,0
        ans = 0
        presum = [0]*(len(nums)+1)
        for right in range(len(nums)):
            
            presum[right+1] = presum[right] + nums[right]
            
            if nums[right] in ans_dict:

                for i in range(left,ans_dict[nums[right]]+1):

                    ans_dict.pop(nums[i])

                left = i+1
                ans_dict[nums[right]] = right

            else:

                ans_dict[nums[right]] = right

            if right-left+1 == k:

                ans = max(ans,presum[right+1]-presum[left])
                ans_dict.pop(nums[left])
                left+=1

        return ans

        