class Solution(object):
    def removeDuplicates(self, nums):
        left=0
        right=1
        count=1
        while right!=len(nums):
            if nums[left]==nums[right]:
                right+=1
            else:
                temp=nums[left+1]
                nums[left+1]=nums[right]
                nums[right]=temp
                left+=1
                right+=1
                count+=1
        return count