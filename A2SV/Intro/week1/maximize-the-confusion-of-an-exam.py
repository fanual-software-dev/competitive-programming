class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def maximum_(letter):
            left = 0
            count = k
            ans=0

            for right in range(len(answerKey)):

                if answerKey[right] != letter:
                    count-=1
                while count<0:

                    if answerKey[left] != letter:
                        count+=1
                    left+=1
                ans = max(ans, right-left+1)
            return ans
        return max(maximum_("T"),maximum_("F"))