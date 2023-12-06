class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive_set = []
        negative_set = []
        ans = []

        for i in nums:
            if i > 0:
                positive_set.append(i)
            else:
                negative_set.append(i)
        for i in range(len(positive_set)):
            ans.append(positive_set[i])
            ans.append(negative_set[i])

        return ans
        