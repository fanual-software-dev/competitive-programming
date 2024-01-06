class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str 
        :type p: str
        :rtype: List[int]
        """
        dictans1={0:0}
        dictans2={0:0}
        n=len(p)
        ans=[]
        for i in p:
            dictans1[i]=1+dictans1.get(i,0)
        left=0
        for right in range(len(s)):
            dictans2[s[right]]=1+dictans2.get(s[right],0)
            if right-left+1==n:
                if dictans2==dictans1:
                    ans.append(left)
                dictans2[s[left]]-=1
                if dictans2[s[left]]==0:
                    dictans2.pop(s[left])
                left+=1
            
        return ans