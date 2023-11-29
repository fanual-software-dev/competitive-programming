class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        st=""
        for i in range(len(strs[0])):
            u=strs[0][i]
            count=1
            for j in range(1,len(strs)):
                z=len(strs[j])
                if i<z:
                    v=strs[j][i]
                    if u==v:
                        count+=1
                    else:
                        break
                else:
                    break
            if count==len(strs):
                st+=u
            else:
                break
        return st