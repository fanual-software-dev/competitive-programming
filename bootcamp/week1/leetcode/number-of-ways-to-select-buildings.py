class Solution:
    def numberOfWays(self, s: str) -> int:

        post0 = [0]*(len(s)+1)
        post1 = [0]*(len(s)+1)

        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                post0[i] = 1 + post0[i+1]
                post1[i] = post1[i+1]
            else:
                post0[i] = post0[i+1]
                post1[i] = 1+post1[i+1]
        ans = 0
        zeroes = 0
        ones = 0
    
        for i in range(len(s)):
            if s[i]=='0':
                zeroes+=1
            else:
                ones+=1
            if s[i]=='0':
                ans+=(ones*post1[i])
            else:
                ans+=(zeroes*post0[i])
        return ans