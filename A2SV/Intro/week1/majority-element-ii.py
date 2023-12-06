class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        dict1={}
        ans=set()

        for i in nums:

            dict1[i]=1+dict1.get(i,0)

            if dict1[i]>len(nums)/3 and i not in ans:
                ans.add(i)
        return ans
        