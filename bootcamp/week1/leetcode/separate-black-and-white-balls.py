class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        count = 0
        for i in range(len(s)):
            if s[i]=='0':
                ans+=i-count
                count+=1
        return ans 

        