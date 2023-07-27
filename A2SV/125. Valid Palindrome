class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        coll=[]
        for i in s:
            if i.isalnum() :
                coll.append(i.lower())
        palindrome="".join(coll)
        return palindrome==palindrome[::-1]
