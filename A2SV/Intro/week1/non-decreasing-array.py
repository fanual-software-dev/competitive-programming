class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i = 0
        while i <len(nums)-1:

            if nums[i]>nums[i+1]:
                original = i
                i+=1
                count = 0
                while i<len(nums)-1:
                    if nums[i]>nums[i+1]:
                        return False
                    if original>0 and nums[i]<nums[original]:
                        count+=1
                    if original>0 and nums[original-1]>nums[original+1] and count==2:
                        return False
                    i+=1
                if original>0 and nums[original-1]>nums[original+1] and original<len(nums)-2 and nums[-1]<nums[original]:
                    return False
            i+=1
        return True
            

        