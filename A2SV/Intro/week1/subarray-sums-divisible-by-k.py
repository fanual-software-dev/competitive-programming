class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        remainder={0:1}
        total=0
        ans=0
    
        for n in nums:

            total+=n
            r=total%k

            ans += remainder.get(r,0)
            remainder[r] = 1+ remainder.get(r,0) 

        return ans