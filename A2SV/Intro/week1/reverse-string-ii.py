class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        ans = []

        for i in s:
            ans.append(i)
        

        for i in range(0,len(ans),2*k):

            ans[i:i+k] = ans[i:i+k][::-1]

        return "".join(ans)
        