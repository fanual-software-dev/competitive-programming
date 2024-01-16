class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.ans=[0,nums[0]]
        for i in range(1,len(self.nums)):
            self.ans.append(self.nums[i]+self.ans[i])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.ans[right+1]-self.ans[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)