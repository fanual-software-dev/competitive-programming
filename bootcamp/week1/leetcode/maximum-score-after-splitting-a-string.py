class Solution:
    def maxScore(self, s: str) -> int:
        presum0 = [0]*(len(s)+1)
        presum1 = [0]*(len(s)+1)

        for i in range(len(s)):
            if s[i]=='0':
                presum0[i+1] = 1+presum0[i]
            else:
                presum0[i+1] = presum0[i]
            
            if s[len(s)-i-1]=='1':
                presum1[len(s)-i-1] = 1+presum1[len(s)-i]
            else:
                presum1[len(s)-i-1] = presum1[len(s)-i]
        ans = 0
        for i in range(1,len(presum1)-1):
            ans = max(ans,presum0[i]+presum1[i])
        return ans

        