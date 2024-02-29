class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check(s):
            se = set(s)

            if len(s)==1:
                return 
            for i in range(len(s)):
                if chr(ord(s[i])-32) in se or chr(ord(s[i])+32) in se:
                    continue
                else:
                    check(s[:i])
                    check(s[i+1:])
                    break
            else:
                if len(s)>len(ans[-1]):
                    ans.pop()
                    ans.append(s)
        ans = ['']
        check(s)
        
        return ans[-1]
        
            

        