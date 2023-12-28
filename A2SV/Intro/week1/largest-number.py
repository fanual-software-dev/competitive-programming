class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)):

            nums[i] = str(nums[i])

        for i in range(1,len(nums)):
            left = i
            while left>0 and nums[left]+nums[left-1]>=nums[left-1]+nums[left]:

                nums[left],nums[left-1] = nums[left-1],nums[left]
                left-=1

        if "".join(nums) in ("0"*100):
            return "0"

        return "".join(nums)



                
        