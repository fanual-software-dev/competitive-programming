class Solution(object):
    def lengthOfLongestSubstring(self, string):
        leng=0
        empty=""    
        for i in string:
            if i not in empty:
                empty=empty+i
                leng=max(leng,len(empty))
            else:
                v=empty.index(i)
                empty=empty[v+1:]+i
        return leng
        