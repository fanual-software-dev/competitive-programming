class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        count=n
        t=0
        i=0
        while count<len(nums):
            
            if t==0:
                ans.append(nums[i])
                t=1
                i+=1
            elif count<len(nums):
                ans.append(nums[count])
                t=0
                count+=1

        return ans