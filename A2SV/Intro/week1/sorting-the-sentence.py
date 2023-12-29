class Solution:
    def sortSentence(self, s: str) -> str:

        ans = s.split()

        for i in range(1,len(ans)):

            left = i
            while left>0 and ans[left][-1]<ans[left-1][-1]:

                ans[left],ans[left-1] = ans[left-1], ans[left]
                left-=1
        for i in range(len(ans)):

            ans[i] = ans[i][:-1]
            
        return " ".join(ans)
        