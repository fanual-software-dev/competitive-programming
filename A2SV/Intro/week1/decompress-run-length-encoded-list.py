class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        num=[]

        for i in range(1,len(nums),2):
            b=nums[i-1]
            num+=[nums[i] for j in range(b)]
        return num
            
        