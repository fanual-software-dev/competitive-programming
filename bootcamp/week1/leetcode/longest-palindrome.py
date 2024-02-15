class Solution:
    def longestPalindrome(self, s: str) -> int:

        dict1 = {}

        for i in s:

            dict1[i] = 1 + dict1.get(i,0)
        ans = 0
        count = 0
    
        for value in dict1.values():

            if value == 1 and count== 0:
                ans+=1
                count+=1
            else:
                if value%2 and count==0:
                    ans+=value
                    count+=1
                else:
                    ans+=(2*(value//2))
        return ans 
        