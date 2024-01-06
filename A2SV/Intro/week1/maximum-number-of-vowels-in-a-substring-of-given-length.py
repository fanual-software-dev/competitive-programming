class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel=["a","e","i","o","u"]
        count=ans=0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        right=k
        left=0
        while right<len(s):
            if ans<count:
                ans=count
            if s[left]  in vowel:
                count-=1
            if s[right] in vowel:
                count+=1
            left+=1
            right+=1
        return max(ans,count)