class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        array=[]
        n=max(candies)

        for i in candies:
            array.append(i+extraCandies>=n)
        return array