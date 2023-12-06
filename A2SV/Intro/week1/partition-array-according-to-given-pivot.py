class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        ans = []

        for i in nums:

            if i < pivot:

                ans.append( i )
        for i in nums:

            if i == pivot:

                ans.append( i )
        for i in nums:
            
            if i > pivot:

                ans.append( i )

        return ans
        