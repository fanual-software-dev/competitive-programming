class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """


        for i in range(left, right+1):

            count=0

            for k in ranges:

                if k[0] <= i and k[1] >= i:

                    count=1
                    break
            if count == 0:

                return False

        return True
