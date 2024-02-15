class Solution:
    def breakPalindrome(self, pal: str) -> str:

        count = 0
        if len(pal)==1:
            return ""
        
        for i in range(len(pal)//2):
            if pal[i]!="a":
                return pal[:i] + "a" + pal[i+1:]
        
        return pal[:len(pal)-1] + "b"  # to handle this kind of test cases aaaabaaaa
        
        