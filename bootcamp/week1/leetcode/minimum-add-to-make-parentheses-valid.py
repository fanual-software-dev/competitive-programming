class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        total = 0
        stack = 0

        for right in s:
            if right==")" and stack==0:
                total+=1
            elif right==")" and stack>0:
                stack-=1
            else:
                stack+=1
        return total + stack


        
        