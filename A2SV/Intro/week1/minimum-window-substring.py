class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ans_dict = defaultdict(int)
        seen = Counter(t)

        ans = " "*10**6
        left = 0

        def check(given1,given2):
            count = 1

            for i in given2:

                if given1[i]<given2[i]:
                    count=0
                    break
            return count

        for right in range(len(s)):

            ans_dict[s[right]]+=1
        
            while left<=right and check(ans_dict,seen):
                ans_dict[s[left]]-=1
                if ans_dict[s[left]]==0:
                    ans_dict.pop(s[left])
    
                if len(ans)>right-left+1:
                    ans = s[left:right+1]
                left+=1 
        
        return ans if ans !=" "*10**6 else ""





        
        