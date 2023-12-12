class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans_dict = {}

        for i in range(len(nums)):

            if target- nums[i] in ans_dict:

                return [ans_dict[target - nums[i]],i]
            ans_dict[nums[i]] = i
        

        
        