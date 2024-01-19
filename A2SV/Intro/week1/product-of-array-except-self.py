class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans_arr=[1]*len(nums)
        ans_arr2=[1]*len(nums)

        for i in range(1,len(nums)):
            ans_arr[i]=ans_arr[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            ans_arr2[i]=ans_arr2[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans_arr[i] = ans_arr[i] * ans_arr2[i]
        return ans_arr        