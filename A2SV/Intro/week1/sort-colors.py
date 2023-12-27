class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for i in range(len(nums)):

            if nums[i]==0:
                nums[left],nums[i] = nums[i],nums[left]
                left+=1
        for j in range(left,len(nums)):

            if nums[j]==1:
                nums[left],nums[j] = nums[j],nums[left]
                left+=1
        

        