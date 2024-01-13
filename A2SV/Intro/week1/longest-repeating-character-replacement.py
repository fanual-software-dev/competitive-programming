class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = {}
        ans = left = maxf = 0
        for right in range(len(s)):
            count[s[right]] = 1+count.get(s[right],0)

            maxf= max(maxf,count[s[right]])

            while (right-left+1) -maxf>k:
                count[s[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans