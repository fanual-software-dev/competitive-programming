class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        ans = left = 0

        for gf in g:

            while left<len(s):

                if s[left]>= gf:
                    ans+=1
                    left+=1
                    break
                else:left+=1
        return ans