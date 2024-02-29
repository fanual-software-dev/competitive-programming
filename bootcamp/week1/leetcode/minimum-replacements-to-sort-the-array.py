class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        number = 0
        valid = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>valid:
                before = nums[i]%valid 
                number+= nums[i]//valid-1 if before==0 else nums[i]//valid
                valid = nums[i]//(nums[i]//valid+1) if before>0 else valid
            else:
                valid = nums[i]
        return number
        